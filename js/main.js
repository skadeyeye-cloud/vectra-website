/* VECTRA International Logistics Ltd — site interactions */
(function () {
  document.documentElement.classList.remove("no-js");

  /* Header state on scroll */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 40);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* Mobile navigation */
  var drawer = document.querySelector(".mobile-nav");
  var openBtn = document.querySelector("[data-menu-open]");
  var closeBtn = document.querySelector("[data-menu-close]");
  function setMenu(open) {
    if (!drawer) return;
    drawer.classList.toggle("is-open", open);
    document.body.classList.toggle("nav-open", open);
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (open && closeBtn) closeBtn.focus();
    if (!open && openBtn) openBtn.focus();
  }
  if (openBtn) openBtn.addEventListener("click", function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setMenu(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && drawer && drawer.classList.contains("is-open")) setMenu(false);
  });

  /* Reveal on scroll */
  var revealables = document.querySelectorAll(".reveal, .map-wrap");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* Footer year */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- Quote / enquiry form ---------- */
  var form = document.querySelector("#quote-form");
  if (!form) return;

  var steps = Array.prototype.slice.call(form.querySelectorAll(".form-step"));
  var indicators = document.querySelectorAll(".steps li");
  var backBtn = form.querySelector("[data-back]");
  var nextBtn = form.querySelector("[data-next]");
  var submitBtn = form.querySelector("[data-submit]");
  var stepError = form.querySelector(".form-error");
  var current = 0;

  // Preselect a service from ?service=vehicle etc.
  var params = new URLSearchParams(window.location.search);
  var pre = params.get("service");
  if (pre) {
    var box = form.querySelector('input[name="services"][value="' + pre + '"]');
    if (box) box.checked = true;
  }

  function showStep(i) {
    current = i;
    steps.forEach(function (s, idx) { s.classList.toggle("is-active", idx === i); });
    indicators.forEach(function (li, idx) {
      li.classList.toggle("is-current", idx === i);
      li.classList.toggle("is-done", idx < i);
    });
    backBtn.hidden = i === 0;
    nextBtn.hidden = i === steps.length - 1;
    submitBtn.hidden = i !== steps.length - 1;
    stepError.classList.remove("is-visible");
    if (i === steps.length - 1) buildReview();
    var top = form.getBoundingClientRect().top + window.scrollY - 120;
    if (window.scrollY > top) window.scrollTo({ top: top, behavior: "smooth" });
  }

  function validateStep(i) {
    var ok = true;
    var step = steps[i];

    if (step.querySelector('input[name="services"]')) {
      if (!step.querySelector('input[name="services"]:checked')) {
        stepError.textContent = "Please select at least one service to continue.";
        stepError.classList.add("is-visible");
        return false;
      }
    }

    step.querySelectorAll("[required]").forEach(function (input) {
      var field = input.closest(".field");
      var valid = input.type === "checkbox" ? input.checked : input.checkValidity() && input.value.trim() !== "";
      if (field) field.classList.toggle("has-error", !valid);
      if (!valid) ok = false;
    });

    if (!ok) {
      stepError.textContent = "Please complete the highlighted fields.";
      stepError.classList.add("is-visible");
      var firstBad = step.querySelector(".has-error input, .has-error select, .has-error textarea");
      if (firstBad) firstBad.focus();
    }
    return ok;
  }

  form.addEventListener("input", function (e) {
    var field = e.target.closest(".field");
    if (field && field.classList.contains("has-error") && e.target.checkValidity()) field.classList.remove("has-error");
  });

  nextBtn.addEventListener("click", function () {
    if (validateStep(current)) showStep(current + 1);
  });
  backBtn.addEventListener("click", function () { showStep(current - 1); });

  function collect() {
    var data = new FormData(form);
    var services = data.getAll("services").map(function (v) {
      var el = form.querySelector('input[name="services"][value="' + v + '"]');
      return el ? el.getAttribute("data-label") : v;
    });
    return {
      services: services.join(", "),
      cargo: data.get("cargo_type") || "",
      origin: data.get("origin") || "",
      destination: data.get("destination") || "",
      volume: data.get("volume") || "",
      timeline: data.get("timeline") || "",
      details: data.get("details") || "",
      name: data.get("name") || "",
      company: data.get("company") || "",
      email: data.get("email") || "",
      phone: data.get("phone") || "",
      method: data.get("contact_method") || ""
    };
  }

  function esc(s) {
    var d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  function buildReview() {
    var d = collect();
    var rows = [
      ["Services", d.services],
      ["Cargo / requirement", d.cargo],
      ["Origin", d.origin],
      ["Destination", d.destination],
      ["Volume / quantity", d.volume],
      ["Timeline", d.timeline]
    ];
    var html = rows.filter(function (r) { return r[1]; }).map(function (r) {
      return "<dt>" + esc(r[0]) + "</dt><dd>" + esc(r[1]) + "</dd>";
    }).join("");
    form.querySelector(".review dl").innerHTML = html;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!validateStep(current)) return;

    var d = collect();
    var endpoint = form.getAttribute("data-endpoint");

    function success() {
      form.querySelector(".form-body").hidden = true;
      document.querySelector(".steps").hidden = true;
      var ok = document.querySelector(".form-success");
      ok.querySelector("[data-name]").textContent = d.name.split(" ")[0] || "there";
      ok.classList.add("is-visible");
      ok.scrollIntoView({ behavior: "smooth", block: "center" });
    }

    if (form.hasAttribute("data-preview")) {
      // Preview deployments have no mail route; say so instead of implying it was sent.
      success();
      document.querySelector(".form-success h2").textContent = "Preview only";
      document.querySelector(".form-success p").textContent = "This form isn't connected yet, so nothing was sent. On the live site, enquiries go to " + (form.getAttribute("data-mailto") || "info@vectralogisticsintl.com") + ".";
      return;
    }

    if (endpoint) {
      // Any JSON/form endpoint (Formspree, Netlify, your CRM, etc.)
      submitBtn.disabled = true;
      fetch(endpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (r) { if (!r.ok) throw new Error(); success(); })
        .catch(function () {
          submitBtn.disabled = false;
          stepError.textContent = "Something went wrong sending your enquiry. Please email us directly at info@vectralogisticsintl.com.";
          stepError.classList.add("is-visible");
        });
      return;
    }

    // No endpoint configured: hand the enquiry to the visitor's email client.
    var body = [
      "QUOTE REQUEST — VECTRA International Logistics",
      "",
      "Services: " + d.services,
      "Cargo / requirement: " + d.cargo,
      "Origin: " + d.origin,
      "Destination: " + d.destination,
      "Volume / quantity: " + d.volume,
      "Timeline: " + d.timeline,
      "",
      "Details:",
      d.details,
      "",
      "Name: " + d.name,
      "Company: " + d.company,
      "Email: " + d.email,
      "Phone: " + d.phone,
      "Preferred contact: " + d.method
    ].join("\n");
    var to = form.getAttribute("data-mailto") || "info@vectralogisticsintl.com";
    window.location.href = "mailto:" + to + "?subject=" + encodeURIComponent("Quote request — " + d.services) + "&body=" + encodeURIComponent(body);
    success();
  });

  showStep(0);
})();
