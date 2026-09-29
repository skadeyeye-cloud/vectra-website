#!/usr/bin/env python3
"""Generates the static VECTRA website into /Users/holysaint/vectra-website."""
import os, html
from worldmap import proj, W as MAP_W, H as MAP_H

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://vectralogisticsintl.com"
EMAIL = "info@vectralogisticsintl.com"
PHONE = "+234 800 000 0000"  # placeholder, replace with the real line
PHONE_HREF = "+2348000000000"

# ---------------------------------------------------------------- icons
P = {
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "down": '<path d="M12 5v14M6 13l6 6 6-6"/>',
 "chev": '<path d="M6 9l6 6 6-6"/>',
 "file": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "headset": '<path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "building": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2M10 21v-3h4v3"/>',
 "landmark": '<path d="M3 21h18M4 10h16M12 3l9 5H3z"/><path d="M6 10v8M10 10v8M14 10v8M18 10v8"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 "leaf": '<path d="M5 19c0-8 5-14 15-14 0 10-6 15-14 15"/><path d="M5 19l7-7"/>',
 "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 21l5-3 5 3-1.5-7"/>',
 "car": '<path d="M3 16v-3l2.2-5A2 2 0 0 1 7 7h10a2 2 0 0 1 1.8 1L21 13v3a1 1 0 0 1-1 1h-1"/><path d="M5 17H4a1 1 0 0 1-1-1M3 13h18M9 17h6"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>',
 "bolt": '<path d="M13 3L5 13h6l-1 8 8-10h-6z"/>',
 "box": '<path d="M3 7.5l9-4.5 9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5l9 4.5 9-4.5M12 12v9"/>',
 "ship": '<path d="M3 16l2 5h14l2-5-9-3z"/><path d="M6 14.5V9h12v5.5M12 9V4M9 6h6"/>',
 "plane": '<path d="M10.5 13.5L3 11l1.5-1.5 8 .5 4-4.5c1-1 2.8-1.3 3.5-.5s.5 2.5-.5 3.5l-4.5 4 .5 8L14 21l-2.5-7.5z"/>',
 "truck": '<path d="M3 6h11v10H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
 "route": '<circle cx="6" cy="18" r="2"/><circle cx="18" cy="6" r="2"/><path d="M8 18h6a3 3 0 0 0 0-6h-4a3 3 0 0 1 0-6h6"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "check": '<path d="M5 12l5 5 9-10"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "close": '<path d="M6 6l12 12M18 6L6 18"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "flag": '<path d="M5 21V4M5 4h12l-2.5 4L17 12H5"/>',
 "message": '<path d="M4 5h16v11H9l-5 4z"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
 "tag": '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
 "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/>',
 "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="17" cy="20" r="1.5"/><path d="M3 4h2l2.5 11h11L21 8H6.5"/>',
 "pill": '<rect x="3" y="8.5" width="18" height="7" rx="3.5" transform="rotate(-45 12 12)"/><path d="M9.5 9.5l5 5"/>',
 "bank": '<path d="M3 21h18M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 10l9-6 9 6z"/>',
 "store": '<path d="M4 9l1.5-5h13L20 9M4 9v11h16V9M4 9a2.7 2.7 0 0 0 5.3 0 2.7 2.7 0 0 0 5.4 0 2.7 2.7 0 0 0 5.3 0"/><path d="M10 20v-5h4v5"/>',
 "food": '<path d="M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10M17 21V3c-2 1-3 4-3 7h3"/>',
 "factory": '<path d="M3 21V10l6 4v-4l6 4V6h6v15z"/><path d="M7 17h2M12 17h2M17 17h2"/>',
 "hospital": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M12 7v6M9 10h6M10 21v-4h4v4"/>',
 "crane": '<path d="M5 21V5h2v16M3 21h8M7 5l12 3M7 5l4-2 8 5M17 8v5"/><rect x="15.5" y="13" width="3" height="3"/>',
 "export": '<path d="M12 15V3M7 8l5-5 5 5"/><path d="M4 14v6h16v-6"/>',
 "import": '<path d="M12 3v12M7 10l5 5 5-5"/><path d="M4 14v6h16v-6"/>',
 "sparkle": '<path d="M12 3l1.8 5.4L19 10l-5.2 1.6L12 17l-1.8-5.4L5 10l5.2-1.6z"/>',
 "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.5V17M8 7.5v.01M12 17v-6.5M12 13.5a2.5 2.5 0 0 1 5 0V17"/>',
 "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/>',
 "x": '<path d="M4 4l16 16M20 4L4 20"/>',
 "facebook": '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z"/>',
}

def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>')

LOGO = ('<svg class="brand__mark" viewBox="0 0 48 48" fill="none" stroke="currentColor" aria-hidden="true">'
        '<circle cx="24" cy="24" r="21.5" stroke-width="1.3"/><ellipse cx="24" cy="24" rx="21.5" ry="9.5" stroke-width="1"/>'
        '<path d="M24 2.5v43M2.5 24h43" stroke-width="0.9"/>'
        '<path d="M12.5 13.5L24 36l11.5-22.5" stroke-width="2.6"/><path d="M18.5 13.5L24 24.5l5.5-11" stroke-width="1.6"/></svg>')

MARK_BIG = LOGO.replace('class="brand__mark"', 'class="mv-card__mark"')

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Crect width='48' height='48' rx='10' fill='%230a1729'/%3E"
           "%3Cg fill='none' stroke='%23c9a45c'%3E%3Ccircle cx='24' cy='24' r='18' stroke-width='1.6'/%3E%3Cpath d='M14.5 15L24 34l9.5-19' stroke-width='3.4'/%3E%3C/g%3E%3C/svg%3E")

A = ic("arrow")

# ---------------------------------------------------------------- data
SERVICES = [
 dict(slug="vehicle", pick="Cars, SUVs & fleets from USA, Europe & Asia", file="vehicle-logistics.html", num="01", name="Vehicle Logistics", icon="car", accent="#c9a45c",
      card="car.jpg", hero="gwagon.jpg", extra="port-cranes.jpg", extra2="port-aerial.jpg",
      short="End-to-end vehicle importation from USA, Europe & Asia with full documentation and insured transit.",
      tagline="Importing precision-engineered vehicles across three continents.",
      intro="From a single luxury SUV to a full corporate fleet, VECTRA sources, ships, clears and delivers vehicles into Nigeria with every document in order. We buy through auctions, dealerships and OEM channels in the USA, UK, Germany, Japan and the UAE, and we stay responsible until the keys are in your hand.",
      chips=[("globe", "USA · UK · Germany · Japan · UAE"), ("crane", "Apapa · Tin Can · Onne"), ("shield", "Insured transit")],
      bullets=["Sourcing from USA, UK, Germany, Japan & UAE", "Full documentation: Bill of Lading, customs, duty",
               "Insured transit with real-time cargo tracking", "Port clearance & final delivery across Nigeria",
               "Dealer & corporate fleet partnerships"],
      clients=[("building", "Corporate fleets"), ("car", "Automobile dealers"), ("landmark", "Government agencies"), ("user", "Private buyers")],
      breakdown=[("car", "What We Import", "Passenger cars, SUVs, commercial trucks, luxury vehicles, and construction equipment from three continents."),
                 ("search", "Sourcing & Procurement", "We inspect and procure to your specification from auctions, dealerships, or OEM channels, with pre-shipment reports."),
                 ("file", "Customs & Clearing", "Expert NCS brokerage at Apapa, Tin Can, and Onne, covering duty, Form M, PAAR, and delivery documentation."),
                 ("layers", "Fleet Solutions", "Bulk importation, tracking, duty scheduling, and pre-delivery inspection for every corporate unit.")],
      process=[("Brief & specification", "Share the make, model, budget and timeline. We confirm the specification, sourcing channel and a landed-cost estimate."),
               ("Sourcing & inspection", "We inspect and procure from auctions, dealerships or OEMs, with a pre-shipment report before you commit."),
               ("Insured shipping", "Vehicles are booked, insured and tracked in real time from the origin port to Nigeria."),
               ("Customs & clearing", "Our NCS brokerage team handles Form M, PAAR, duty and terminal release at Apapa, Tin Can and Onne."),
               ("Delivery & handover", "Final delivery anywhere in Nigeria, with pre-delivery inspection and a complete document pack.")],
      deliverables=[("Pre-shipment inspection report", "Condition, history and specification verified at source."),
                    ("Bill of Lading & shipping docs", "Every transit document prepared and checked."),
                    ("Duty, Form M & PAAR", "Customs assessment and processing handled end to end."),
                    ("Insured transit", "Cover from origin port to final delivery."),
                    ("Real-time cargo tracking", "Know where your vehicle is at every stage."),
                    ("Pre-delivery inspection", "Handover with a full document pack.")]),
 dict(slug="last-mile", pick="GPS-tracked e-bike delivery in Abuja & Lagos", file="electric-last-mile.html", num="02", name="Electric Last-Mile", icon="bolt", accent="#5fc9a0",
      card="scooter.jpg", hero="scooter.jpg", extra="courier.jpg", extra2="warehouse-boxes.jpg",
      short="Sustainable, GPS-tracked urban e-bike delivery across Abuja, Lagos, and expanding Nigerian cities.",
      tagline="Sustainable, precision-tracked urban delivery across Nigerian cities.",
      intro="VECTRA's electric fleet moves parcels, prescriptions, documents and orders across the city without burning fuel. Every rider is assigned and insured, every trip is GPS-tracked, and every delivery ends with proof. Your customers get speed and you get certainty.",
      chips=[("pin", "Abuja · Lagos · expanding"), ("clock", "Same-day & scheduled"), ("leaf", "Zero emissions")],
      bullets=["E-bike delivery fleet: zero emissions, low cost", "Real-time tracking via dedicated dispatch platform",
               "Same-day and scheduled delivery windows", "Coverage across Abuja, Lagos & expanding cities",
               "Green logistics: reduced carbon per delivery"],
      clients=[("cart", "E-commerce"), ("pill", "Pharmacies"), ("bank", "Banks"), ("store", "Retailers"), ("food", "Food brands"), ("users", "SMEs")],
      breakdown=[("bolt", "The Fleet", "GPS-tracked cargo e-bikes and electric three-wheelers optimised for Nigerian urban terrain, rider-assigned and insured."),
                 ("message", "How It Works", "Order by call, WhatsApp, or API. Dispatch assigns the nearest rider with a real-time ETA and proof of delivery."),
                 ("box", "Business Use Cases", "E-commerce fulfilment, pharma last-mile, food delivery, document courier, and bank instrument dispatch."),
                 ("leaf", "Why Electric", "Lower cost per delivery, zero fuel dependency and reduced maintenance, aligned with corporate ESG goals.")],
      process=[("Place an order", "Book by phone, WhatsApp, or plug our dispatch into your store through the API."),
               ("Smart dispatch", "The nearest available rider is assigned and heads straight to pickup."),
               ("Live tracking", "A real-time ETA is shared with you and your customer."),
               ("Proof of delivery", "Every drop is confirmed on handover, so nothing goes missing without a trace."),
               ("Reporting", "Delivery records to support reconciliation and your ESG reporting.")],
      deliverables=[("Same-day & scheduled windows", "Delivery slots that fit your customers."),
                    ("GPS tracking on every order", "Live location and ETA, end to end."),
                    ("Proof of delivery", "Confirmed handover on each drop."),
                    ("Insured, assigned riders", "Accountable handling for every parcel."),
                    ("Call, WhatsApp or API ordering", "Book however your team works."),
                    ("Lower carbon per delivery", "Electric vehicles, zero fuel.")]),
 dict(slug="procurement", pick="Supplier vetting, sourcing & QA", file="procurement.html", num="03", name="Procurement Services", icon="box", accent="#d6905f",
      card="warehouse-boxes.jpg", hero="warehouse.jpg", extra="warehouse-boxes.jpg", extra2="containers.jpg",
      short="Global sourcing with supplier vetting, quality assurance, and full order-lifecycle management.",
      tagline="Sourcing the right goods from the right suppliers, globally.",
      intro="Buying internationally shouldn't mean trusting a stranger with your capital. VECTRA identifies, vets and manages suppliers for you, then carries the order through inspection, shipping, customs and delivery, with itemised landed costs quoted upfront.",
      chips=[("tag", "Binding quotes"), ("search", "Factory audits"), ("shield", "No hidden fees")],
      bullets=["Global supplier identification & vetting", "Specification development & RFQ management",
               "Price benchmarking and negotiation", "Pre-shipment inspection & quality assurance",
               "Full import documentation & customs management"],
      clients=[("factory", "Manufacturers"), ("hospital", "Hospitals"), ("crane", "Construction firms"), ("landmark", "Government agencies"), ("store", "Retailers")],
      breakdown=[("box", "What We Source", "Industrial equipment, construction materials, medical supplies, electronics, raw materials, and machinery."),
                 ("search", "Supplier Vetting", "Due diligence on international suppliers, verifying registration, track record, and quality through factory audits."),
                 ("clipboard", "Order Management", "From PO issuance through production monitoring, inspection, export documents, and final delivery."),
                 ("tag", "Cost Transparency", "Itemised breakdowns of goods, freight, insurance, duties, and landed costs. No hidden fees; binding quotes.")],
      process=[("Specification & RFQ", "We turn your requirement into a clear specification and run the request for quotation."),
               ("Supplier vetting", "Registration, track record and quality are verified, including factory audits where needed."),
               ("Benchmark & negotiate", "Prices are benchmarked and terms negotiated in your favour before a PO is issued."),
               ("Production & inspection", "We monitor production and inspect goods before they ship."),
               ("Ship, clear & deliver", "Export docs, freight, customs and final delivery under one accountable team.")],
      deliverables=[("Vetted supplier shortlist", "Verified partners, not directory listings."),
                    ("Specification & RFQ pack", "Clear requirements suppliers can quote against."),
                    ("Price benchmark", "Know what fair value looks like."),
                    ("Pre-shipment inspection report", "Quality confirmed before goods leave."),
                    ("Itemised, binding landed-cost quote", "Goods, freight, insurance and duties."),
                    ("Export & import documentation", "Complete and compliant.")]),
 dict(slug="freight", pick="Sea, air & road freight with NCS clearance", file="freight-customs.html", num="04", name="Freight & Customs", icon="ship", accent="#6fa8dc",
      card="plane.jpg", hero="ship-aerial.jpg", extra="truck-scania.jpg", extra2="port-cranes.jpg",
      short="Sea, air & road freight with licensed NCS customs brokerage at all major Nigerian ports.",
      tagline="Moving cargo across borders with precision and full compliance.",
      intro="Sea, air or road, VECTRA books the right mode for your cargo and clears it with licensed customs agents who know Nigerian terminals inside out. HS classification, duty optimisation and documentation are settled before your cargo arrives, not after it's held.",
      chips=[("ship", "FCL · LCL · Air · Road"), ("crane", "Apapa · Tin Can · Onne"), ("route", "ECOWAS corridors")],
      bullets=["Sea freight: FCL & LCL from major global ports", "Air freight for time-critical, high-value cargo",
               "Road haulage across Nigerian & border corridors", "Full NCS brokerage at Apapa, Tin Can, Onne",
               "Bonded warehousing & cargo consolidation"],
      clients=[("import", "Importers"), ("export", "Exporters"), ("factory", "Manufacturers"), ("store", "Retailers"), ("users", "NGOs"), ("landmark", "Government agencies")],
      breakdown=[("ship", "Sea Freight", "FCL and LCL from China, the USA, UK, India, and UAE, with vessel booking, BL coordination, and discharge operations."),
                 ("plane", "Air Freight", "Express and consolidated air freight via Lagos, Abuja, and Kano for time-sensitive, high-value cargo."),
                 ("file", "Customs Brokerage", "Licensed agents for HS classification, duty optimisation, Form M, PAAR, NESS, and terminal exit."),
                 ("truck", "Inland Haulage", "Bonded trucking from port to destination across Lagos, Abuja, Kano, Port Harcourt, and cross-border ECOWAS routes.")],
      process=[("Quote & mode selection", "We match your cargo to the right mode: FCL, LCL, air or road."),
               ("Booking & documentation", "Vessel or flight booking, BL coordination and Form M prepared in advance."),
               ("Transit & tracking", "Your cargo is monitored from origin to discharge."),
               ("Customs brokerage", "HS classification, duty, PAAR, NESS and terminal exit by licensed agents."),
               ("Haulage & delivery", "Bonded trucking to your door across Nigeria and ECOWAS routes.")],
      deliverables=[("FCL & LCL sea freight", "From China, USA, UK, India and UAE."),
                    ("Express & consolidated air", "Via Lagos, Abuja and Kano."),
                    ("HS classification & duty optimisation", "Pay the right duty, no more."),
                    ("Form M, PAAR & NESS", "Processed by licensed agents."),
                    ("Bonded warehousing", "Secure storage and consolidation."),
                    ("Inland & ECOWAS haulage", "Bonded trucking to destination.")]),
 dict(slug="advisory", pick="Corridor design, risk & vendor strategy", file="supply-chain-advisory.html", num="05", name="Supply Chain Advisory", icon="route", accent="#b9c6da",
      card="meeting.jpg", hero="meeting.jpg", extra="port-aerial.jpg", extra2="office.jpg",
      short="Corridor design, risk & resilience planning, and vendor strategy consulting for enterprise clients.",
      tagline="Transforming complex logistics challenges into competitive advantages.",
      intro="Most supply chains aren't designed; they pile up over time. VECTRA's advisory team audits how your goods actually move, finds where cost and risk are leaking out, and designs corridors, contingencies and vendor structures that hold up under pressure.",
      chips=[("building", "Enterprise clients"), ("shield", "Risk & resilience"), ("chart", "Landed-cost optimisation")],
      bullets=["Supply chain audit & performance assessment", "Corridor design & freight route optimisation",
               "Risk management & resilience planning", "Vendor management & supplier strategy",
               "Cost reduction & landed cost optimisation"],
      clients=[("globe", "Multinationals"), ("factory", "Manufacturers"), ("import", "Importers"), ("store", "Retailers"), ("bank", "Banks"), ("landmark", "Government agencies")],
      breakdown=[("search", "Supply Chain Audit", "End-to-end assessments that identify bottlenecks, cost leakages, compliance gaps, and optimisation opportunities."),
                 ("route", "Corridor Design", "Optimal freight corridors: the right ports, modes, customs pathways, and last-mile strategies for your cargo."),
                 ("shield", "Risk & Resilience", "Contingency frameworks with alternative suppliers, backup routes, bonded storage, and force-majeure protocols."),
                 ("users", "Vendor Strategy", "Structured vendor relationships with quality benchmarks, payment terms, KPIs, and buyer-protective contracts.")],
      process=[("Discovery", "We map your goods, suppliers, corridors and the outcomes that matter to your business."),
               ("Audit & diagnosis", "Bottlenecks, cost leakages and compliance gaps are identified and quantified."),
               ("Corridor design", "We specify the right ports, modes, customs pathways and last-mile strategy."),
               ("Resilience planning", "Backup suppliers, alternate routes and force-majeure protocols are put in place."),
               ("Implementation & KPIs", "We help roll the changes out and set KPIs to track performance.")],
      deliverables=[("Supply chain audit report", "A clear picture of how goods really move."),
                    ("Landed-cost model", "Where money is lost and how to recover it."),
                    ("Corridor design blueprint", "Ports, modes and customs pathways specified."),
                    ("Risk & contingency framework", "Prepared before disruption hits."),
                    ("Vendor strategy & KPI scorecard", "Suppliers held to measurable standards."),
                    ("Implementation roadmap", "Prioritised, owned and time-bound.")]),
]
SVC = {s["slug"]: s for s in SERVICES}

INDUSTRIES = [
 dict(name="Automotive & Fleet", img="suv.jpg", icon="car",
      desc="Importers, dealers, and fleet managers needing precision-timed vehicle delivery.",
      long="Vehicles are high-value, document-heavy and time-sensitive. We give dealers and fleet managers a single partner that sources, ships, clears and delivers, so stock lands when it's needed and every unit arrives with clean paperwork.",
      needs=["Precision-timed arrivals for sales and fleet rollouts", "Clean documentation and clear duty costs", "Pre-delivery inspection on every unit", "Bulk importation and duty scheduling"],
      svcs=["vehicle", "freight", "procurement"]),
 dict(name="Enterprise & Industry", img="truck-scania.jpg", icon="factory",
      desc="Manufacturers requiring predictable multi-corridor distribution infrastructure.",
      long="Production lines can't wait on a delayed container. We build predictable, multi-corridor supply for manufacturers: vetted suppliers, compliant clearance and bonded haulage, with the full landed cost visible before you commit.",
      needs=["Predictable lead times across several corridors", "Vetted suppliers for equipment and raw materials", "No surprises at Nigerian ports", "Visibility down to landed cost"],
      svcs=["procurement", "freight", "advisory"]),
 dict(name="Urban E-Commerce", img="courier.jpg", icon="cart",
      desc="Online retailers requiring sustainable, precision-tracked last-mile delivery.",
      long="For online brands, delivery is the customer experience. Our electric last-mile fleet brings same-day speed, live tracking and proof of delivery to Abuja and Lagos at a lower cost per drop, and with a greener footprint.",
      needs=["Same-day and scheduled delivery windows", "Live tracking your customers can follow", "Proof of delivery on every order", "Lower cost per delivery"],
      svcs=["last-mile", "freight", "advisory"]),
 dict(name="Government & NGOs", img="gov.jpg", icon="landmark",
      desc="Public-sector agencies requiring scalable, transparent international supply solutions.",
      long="Public programmes demand accountability at every step. We deliver transparent, auditable international procurement and logistics, from vetted suppliers and itemised costs to compliant clearance and resilient contingency planning.",
      needs=["Transparent, auditable procurement", "International supply that scales", "Compliance-first customs clearance", "Contingency plans for critical supplies"],
      svcs=["procurement", "freight", "advisory", "vehicle"]),
]

WHY = [
 ("globe", "3-Continent Reach", "Active networks in the USA, Europe, and Asia. We own the corridor, not just the freight booking.",
  ["Sourcing across the USA, UK, Germany, Japan, UAE, China and India", "Established routes into Apapa, Tin Can, Onne and major airports", "One team coordinating origin to destination"]),
 ("target", "Zero-Error Standard", "Every shipment is governed by a zero-margin protocol. We prevent failure before it occurs.",
  ["Documentation verified before cargo moves", "Pre-shipment inspection on vehicles and procured goods", "Insured transit with real-time tracking"]),
 ("flag", "Nigerian Market Depth", "Deep NCS, FAAN, and port expertise. No surprises at Nigerian clearance terminals.",
  ["Licensed NCS customs brokerage", "Form M, PAAR, NESS and HS classification handled in-house", "Bonded warehousing and inland haulage"]),
 ("layers", "End-to-End Ownership", "From procurement to final delivery: one contact, full accountability, zero gaps.",
  ["A single point of contact for every shipment", "Itemised, binding quotes with no hidden fees", "Procurement, freight, clearance and last-mile under one roof"]),
]

VALUES = [
 ("target", "Absolute Precision", "Zero margin for error across customs boundaries, transit corridors, and terminal operations. Every shipment is a commitment."),
 ("award", "The Gold Standard", "Elite, white-glove accountability across all asset transit protocols, with full transparency and structural integrity at every stage."),
 ("compass", "Global Agility", "Navigating volatile regulatory and cross-border environments through live intelligence and deep localised expertise across three continents."),
 ("leaf", "Forward Stewardship", "Protecting clients' capital, cargo, and environmental footprints through optimised routing and responsible trade partnerships."),
]

# ---------------------------------------------------------------- layout
NAV = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"),
       ("industries.html", "Industries"), ("why-vectra.html", "Why VECTRA"), ("contact.html", "Contact")]

def header(active):
    items = []
    for href, label in NAV:
        if href == "services.html":
            sub = "".join(f'<li><a href="{s["file"]}"><span class="num">{s["num"]}</span>{s["name"]}</a></li>' for s in SERVICES)
            is_act = ' is-active' if active == "services" else ''
            items.append(
                f'<li class="has-dropdown{is_act}"><a class="nav__toggle" href="services.html"{" aria-current=\"page\"" if active=="services-index" else ""}>Services {ic("chev")}</a>'
                f'<ul class="dropdown">{sub}<li><a class="all" href="services.html">All services {ic("arrow")}</a></li></ul></li>')
        else:
            cur = ' aria-current="page"' if href == active else ""
            items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    mob_sub = "".join(f'<a href="{s["file"]}">{s["num"]} &nbsp;{s["name"]}</a>' for s in SERVICES)
    mob = []
    for href, label in NAV:
        mob.append(f'<li><a href="{href}">{label}</a>' + (f'<div class="sub">{mob_sub}</div>' if href == "services.html" else "") + '</li>')
    brand = (f'<a class="brand" href="index.html" aria-label="VECTRA International Logistics, home">{LOGO}'
             '<span class="brand__text"><span class="brand__name">VECTRA</span><span class="brand__sub">INTERNATIONAL LOGISTICS LTD</span></span></a>')
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    {brand}
    <nav aria-label="Primary"><ul class="nav__links">{"".join(items)}</ul></nav>
    <div class="nav__cta">
      <a class="btn btn--gold btn--sm" href="contact.html">Get a Quote {A}</a>
      <button class="menu-btn" type="button" data-menu-open aria-controls="mobile-nav" aria-expanded="false" aria-label="Open menu">{ic("menu")}</button>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobile-nav" aria-hidden="true">
  <div class="mobile-nav__top">{brand}<button class="menu-btn" type="button" data-menu-close aria-label="Close menu" style="display:grid">{ic("close")}</button></div>
  <ul>{"".join(mob)}</ul>
  <a class="btn btn--gold" href="contact.html">Get a Quote {A}</a>
</div>'''

def footer():
    svc_links = "".join(f'<li><a href="{s["file"]}">{s["name"]}</a></li>' for s in SERVICES)
    quick = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)
    socials = "".join(f'<a href="#" aria-label="VECTRA on {n.title()}">{ic(n)}</a>' for n in ["linkedin", "instagram", "x", "facebook"])
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html" aria-label="VECTRA home">{LOGO}<span class="brand__text"><span class="brand__name">VECTRA</span><span class="brand__sub">INTERNATIONAL LOGISTICS LTD</span></span></a>
        <p class="tag">Precision in Motion.</p>
        <p>Premium freight, trading, and supply chain solutions connecting Nigeria to global opportunity.</p>
        <!-- TODO: replace # with the real social profile URLs -->
        <div class="socials">{socials}</div>
      </div>
      <div><h4>Quick Links</h4><ul>{quick}</ul></div>
      <div><h4>Our Services</h4><ul>{svc_links}</ul></div>
      <div>
        <h4>Contact Us</h4>
        <ul class="contact-list">
          <li>{ic("pin")}<span>Abuja, FCT, Nigeria</span></li>
          <li>{ic("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <!-- TODO: replace placeholder phone number -->
          <li>{ic("phone")}<a href="tel:{PHONE_HREF}">{PHONE}</a></li>
          <li>{ic("globe")}<span>United States · Europe · Asia</span></li>
        </ul>
        <a class="btn btn--gold btn--sm" href="contact.html">Get a Quote {A}</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> VECTRA International Logistics Ltd. All rights reserved.</span>
      <span>vectralogisticsintl.com</span>
    </div>
  </div>
</footer>'''

def page(fname, title, desc, body, active, accent=None):
    style = f' style="--accent:{accent}"' if accent else ""
    full_title = title if fname == "index.html" else f"{title} | VECTRA International Logistics"
    url = SITE + "/" + ("" if fname == "index.html" else fname)
    doc = f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#05080f">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="VECTRA International Logistics Ltd">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/port-cranes.jpg">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
</head>
<body{style}>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="js/main.js"></script>
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w").write(doc)
    print("wrote", fname)

# ---------------------------------------------------------------- shared blocks
def cta(title="Let’s Build Your Corridor.", lead="VECTRA is ready to architect your next global supply chain solution, from vehicle importation to last-mile electric delivery and from strategic procurement to freight corridors. We are your precision partner.", img="port-night.jpg", service=None):
    q = f"?service={service}" if service else ""
    return f'''<section class="cta">
  <div class="cta__bg"><img src="images/{img}" alt="" loading="lazy"></div>
  <div class="container">
    <div class="reveal" style="max-width:720px">
      <p class="eyebrow">Ready to move forward?</p>
      <h2>{title}</h2>
      <p class="lead">{lead}</p>
      <div class="btn-row">
        <a class="btn btn--gold" href="contact.html{q}">Get a Quote {A}</a>
        <a class="btn btn--ghost" href="mailto:{EMAIL}">Speak to Our Team</a>
      </div>
    </div>
    <ul class="assurances">
      <li>{ic("file")}Full Documentation</li>
      <li>{ic("shield")}Insured Transit</li>
      <li>{ic("pin")}Real-Time Tracking</li>
      <li>{ic("headset")}Dedicated Support</li>
    </ul>
  </div>
</section>'''

def corridor_map():
    hub = proj(8, 9.5)
    origins = [("USA", proj(-98, 39), (-28, -18), "end"), ("Europe", proj(10, 50), (16, -12), "start"), ("Asia", proj(112, 33), (16, -12), "start")]
    arcs, glows, nodes = [], [], []
    for i, (label, (x, y), (dx, dy), anchor) in enumerate(origins):
        hx, hy = hub
        mx, my = (x + hx) / 2, (y + hy) / 2
        dist = ((hx - x) ** 2 + (hy - y) ** 2) ** 0.5
        cx, cy = mx, my - dist * 0.32
        d = f"M{x:.1f} {y:.1f} Q{cx:.1f} {cy:.1f} {hx:.1f} {hy:.1f}"
        arcs.append(f'<path class="arc" d="{d}"/>')
        glows.append(f'<path class="arc-glow" d="{d}" style="animation-delay:{i*0.7:.1f}s"/>')
        nodes.append(f'<g class="node"><circle class="pulse" cx="{x:.1f}" cy="{y:.1f}" r="9" style="animation-delay:{i*0.5:.1f}s"/>'
                     f'<circle class="core" cx="{x:.1f}" cy="{y:.1f}" r="7"/>'
                     f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}">{label}</text></g>')
    hx, hy = hub
    nodes.append(f'<g class="node node--hub"><circle class="pulse" cx="{hx:.1f}" cy="{hy:.1f}" r="12"/>'
                 f'<circle class="core" cx="{hx:.1f}" cy="{hy:.1f}" r="9"/>'
                 f'<text x="{hx+18:.1f}" y="{hy+30:.1f}">Nigeria</text></g>')
    return (f'<div class="map-wrap"><svg class="map-svg" viewBox="0 0 {MAP_W} {MAP_H}" role="img" '
            'aria-label="Map of VECTRA corridors from the USA, Europe and Asia into Nigeria">'
            f'<image class="map-dots" href="images/world-dots.svg" width="{MAP_W}" height="{MAP_H}"/>'
            + "".join(arcs) + "".join(glows) + "".join(nodes) + '</svg></div>')

def page_hero(eyebrow, title, lead, img, crumbs=None, extra="", cls=""):
    cr = ""
    if crumbs:
        parts = ['<a href="index.html">Home</a>']
        for href, label in crumbs:
            parts.append('<span aria-hidden="true">/</span>')
            parts.append(f'<a href="{href}">{label}</a>' if href else f'<span>{label}</span>')
        cr = f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'
    return f'''<section class="page-hero {cls}">
  <div class="page-hero__bg"><img src="images/{img}" alt="" fetchpriority="high"></div>
  <div class="container">
    {cr}
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div>
</section>'''

def svc_cards():
    out = []
    for i, s in enumerate(SERVICES):
        out.append(f'''<a class="svc-card reveal" style="--d:{i*0.08:.2f}s" href="{s["file"]}">
      <div class="svc-card__img"><img src="images/{s["card"]}" alt="" loading="lazy"></div>
      <div class="svc-card__body">
        <span class="svc-card__num">{s["num"]}</span>
        <h3>{s["name"]}</h3>
        <p>{s["short"]}</p>
        <span class="go" aria-hidden="true">{ic("arrow")}</span>
      </div>
    </a>''')
    return "\n    ".join(out)

def ind_cards():
    return "\n    ".join(f'''<article class="ind-card reveal" style="--d:{i*0.08:.2f}s">
      <div class="ind-card__img"><img src="images/{d["img"]}" alt="" loading="lazy"></div>
      <div class="ind-card__body"><h3>{d["name"]}</h3><p>{d["desc"]}</p></div>
    </article>''' for i, d in enumerate(INDUSTRIES))

def why_features():
    return "\n      ".join(f'''<article class="feature reveal" style="--d:{i*0.08:.2f}s">
        <div class="icon-circle">{ic(icon)}</div>
        <h3>{t}</h3>
        <p>{d}</p>
      </article>''' for i, (icon, t, d, _) in enumerate(WHY))

def bullets(items):
    return '<ul class="bullets">' + "".join(f'<li>{ic("check")}<span>{b}</span></li>' for b in items) + '</ul>'

# ---------------------------------------------------------------- HOME
home = f'''<section class="hero">
  <div class="hero__bg"><img src="images/port-cranes.jpg" alt="" fetchpriority="high"></div>
  <div class="container">
    <div class="hero__content">
      <p class="eyebrow eyebrow--plain hero__eyebrow">VECTRA International Logistics Ltd</p>
      <h1>Precision <span class="gold">in Motion.</span></h1>
      <p class="hero__lead">Premium freight, trading, and supply chain solutions connecting Nigeria to global opportunity.</p>
      <div class="btn-row">
        <a class="btn btn--gold" href="contact.html">Get a Quote {A}</a>
        <a class="btn btn--ghost" href="services.html">Our Services</a>
      </div>
    </div>
    <div class="hero__foot">
      <div class="route" aria-label="Corridors: USA, Europe and Asia to Nigeria">
        <span>USA</span><span class="sep"></span><span>Europe</span><span class="sep"></span><span>Asia</span>{ic("arrow")}<strong>Nigeria</strong>
      </div>
      <a class="scroll-cue" href="#reach" aria-label="Scroll to content">{ic("down")}</a>
    </div>
  </div>
</section>

<section class="corridor-band" id="reach" aria-label="Global reach">
  <div class="container corridor-band__inner">
    <span class="label">Global reach</span>
    <ul class="corridor-list">
      <li>United States <small>Vehicles · Freight</small></li>
      <li>Europe <small>UK · Germany</small></li>
      <li>Asia <small>Japan · China · India · UAE</small></li>
      <li class="arrow" aria-hidden="true">{ic("arrow")}</li>
      <li><span class="dest">Nigeria</span> <small>Apapa · Tin Can · Onne</small></li>
    </ul>
  </div>
</section>

<section class="section section--cream" id="about">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">About VECTRA</p>
      <h2>Global Logistics.<br>Real Opportunities.</h2>
      <p class="lead" style="margin-top:24px">Founded in 2026 and headquartered in Abuja, Nigeria, VECTRA International Logistics Ltd is a premium freight, trading, and supply chain solutions company built for the demands of global commerce.</p>
      <p>We specialise in vehicle logistics from the USA, Europe, and Asia, moving high-value automobiles and commercial fleets with full documentation. Beyond vehicles, we operate across electric last-mile delivery, strategic procurement, freight &amp; customs, and supply chain advisory.</p>
      <a class="btn btn--gold" href="about.html" style="margin-top:18px">Learn More About Us {A}</a>
    </div>
    <div class="media-stack reveal" style="--d:.15s">
      <div class="media-stack__img"><img src="images/port-aerial.jpg" alt="Aerial view of a container port with cranes and stacked containers" loading="lazy"></div>
      <div class="fact-card">
        <ul>
          <li><span class="icon-circle">{ic("calendar")}</span><span><small>Founded</small><strong>2026</strong></span></li>
          <li><span class="icon-circle">{ic("pin")}</span><span><small>Headquarters</small><strong>Abuja, Nigeria</strong></span></li>
          <li><span class="icon-circle">{ic("globe")}</span><span><small>Operational reach</small><strong>3 Continents</strong></span></li>
          <li><span class="icon-circle">{ic("layers")}</span><span><small>Core services</small><strong>5 Business Lines</strong></span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section dark" id="services">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow eyebrow--center">Our Services</p>
      <h2>Five Integrated Service Lines.</h2>
      <p class="lead">Spanning the entire international trade lifecycle, from sourcing and shipping to clearance and final delivery.</p>
    </div>
    <div class="services-grid">
    {svc_cards()}
    </div>
  </div>
</section>

<section class="section section--white" id="industries">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow eyebrow--center">Target Markets</p>
      <h2>Industries We Power.</h2>
      <p class="lead">Tailored solutions for high-impact sectors.</p>
    </div>
    <div class="ind-grid">
    {ind_cards()}
    </div>
    <div style="text-align:center;margin-top:48px" class="reveal"><a class="link-arrow" href="industries.html">Explore industries {A}</a></div>
  </div>
</section>

<section class="why-hero" id="why">
  <div class="why-hero__img"><img src="images/gwagon.jpg" alt="" loading="lazy"></div>
  <div class="container">
    <div class="why-hero__text reveal">
      <p class="eyebrow">Why VECTRA</p>
      <h2>More Than Freight.<br>We Offer Architecture.</h2>
      <p class="lead" style="margin-top:22px">VECTRA transforms volatile international trade lanes into highly predictable enterprise advantages. Where standard freight forwarders offer transit, VECTRA offers architecture.</p>
    </div>
  </div>
</section>
<section class="section--tight" style="padding-top:0;background:var(--bg)">
  <div class="container">
    <div class="feature-grid">
      {why_features()}
    </div>
    <div style="margin-top:40px" class="reveal"><a class="link-arrow" href="why-vectra.html">Why clients choose VECTRA {A}</a></div>
  </div>
</section>

<section class="section section--cream" id="corridors">
  <div class="container split split--map">
    <div class="reveal">
      <p class="eyebrow">Global Corridors</p>
      <h2>Connecting Continents. Powering Nigeria.</h2>
      <p class="lead" style="margin:22px 0 28px">Active networks across the USA, Europe, and Asia, moving goods, vehicles, and opportunities into Nigeria with absolute precision.</p>
      {bullets(["Vehicle sourcing from the USA, UK, Germany, Japan & UAE", "Sea freight from China, the USA, UK, India & UAE", "Clearance at Apapa, Tin Can & Onne, with air via Lagos, Abuja & Kano"])}
      <a class="btn btn--gold" href="why-vectra.html" style="margin-top:32px">Our Global Network {A}</a>
    </div>
    <div class="reveal" style="--d:.15s">{corridor_map()}</div>
  </div>
</section>

{cta()}'''
page("index.html", "VECTRA International Logistics Ltd | Precision in Motion.",
     "Premium freight, trading and supply chain solutions connecting Nigeria to global opportunity. Vehicle logistics, electric last-mile, procurement, freight & customs and supply chain advisory from Abuja.",
     home, "index.html")

# ---------------------------------------------------------------- ABOUT
stats = '''<div class="stat-row">
      <div><div class="stat__value">2026</div><div class="stat__label">Founded</div></div>
      <div><div class="stat__value">Abuja</div><div class="stat__label">Headquarters</div></div>
      <div><div class="stat__value">3</div><div class="stat__label">Continents</div></div>
      <div><div class="stat__value">5</div><div class="stat__label">Business Lines</div></div>
    </div>'''
values_html = "".join(f'''<div class="value reveal" style="--d:{i*0.08:.2f}s">
        <div class="icon-circle icon-circle--solid">{ic(icon)}</div>
        <h3>{t}</h3><p>{d}</p></div>''' for i, (icon, t, d) in enumerate(VALUES))
about_svcs = "".join(f'''<a class="other-svc reveal" style="--svc-accent:{s["accent"]};--d:{i*0.06:.2f}s" href="{s["file"]}">
        <span class="n">{s["num"]}</span>
        <div class="row"><h3>{s["name"]}</h3>{ic("arrow")}</div></a>''' for i, s in enumerate(SERVICES))
about = f'''{page_hero("About", "Architecting Global Opportunities.", "We do not simply move cargo. We architect seamless, transparent corridors that turn complex international trade into a competitive advantage for our clients.", "office.jpg", [(None, "About")], stats)}

<section class="section section--white">
  <div class="container split">
    <div class="story-img reveal"><img src="images/port-aerial.jpg" alt="Aerial view of a container terminal" loading="lazy"></div>
    <div class="reveal" style="--d:.12s">
      <p class="eyebrow">Our Story</p>
      <h2>Built for the Demands of Global Commerce.</h2>
      <p class="lead" style="margin-top:24px">Founded in 2026 and headquartered in Abuja, Nigeria, VECTRA International Logistics Ltd is a premium freight, trading, and supply chain solutions company.</p>
      <p>We specialise in vehicle logistics from the USA, Europe, and Asia, moving high-value automobiles and commercial fleets with full documentation. Beyond vehicles, we operate across electric last-mile delivery, strategic procurement, freight &amp; customs, and supply chain advisory.</p>
      <p>Our clients range from automobile dealers and corporate fleets to manufacturers, online retailers, banks and public-sector agencies. What they share is a need for certainty in markets that rarely offer it.</p>
      <p class="pull">“Where standard freight forwarders offer transit, VECTRA offers architecture.”</p>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow eyebrow--center">Mission &amp; Vision</p>
      <h2>Purpose-Driven Logistics.</h2>
    </div>
    <div class="mv-grid">
      <article class="mv-card mv-card--navy reveal">
        <div class="mv-card__head"><span class="mv-card__badge">M</span><h3>Our Mission</h3></div>
        <p>To deliver flawless, end-to-end logistics and trade solutions that connect Nigerian enterprise to global opportunity, moving vehicles, commodities, and capital across borders with absolute precision, unwavering integrity, and zero tolerance for supply chain failure.</p>
        {MARK_BIG}
      </article>
      <article class="mv-card mv-card--gold reveal" style="--d:.12s">
        <div class="mv-card__head"><span class="mv-card__badge">V</span><h3>Our Vision</h3></div>
        <p>To be West Africa’s foremost international logistics and trade company: the definitive gold standard for cross-border freight precision, trusted by multinational enterprises, and recognised globally as the infrastructure that powers Nigeria’s place in international commerce.</p>
      </article>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow eyebrow--center">Our Core Values</p>
      <h2>The Principles We Move By.</h2>
      <p class="lead">The principles that govern every corridor we build and every shipment we move.</p>
    </div>
    <div class="values">{values_html}</div>
  </div>
</section>

<section class="section section--tight dark dark--deep">
  <div class="container">
    <div class="section-head reveal" style="margin-bottom:36px">
      <p class="eyebrow">What We Do</p>
      <h2>Five Business Lines. One Accountable Partner.</h2>
    </div>
    <div class="other-svcs other-svcs--5">{about_svcs}</div>
  </div>
</section>

{cta()}'''
page("about.html", "About Us", "VECTRA International Logistics Ltd: founded in 2026 in Abuja, Nigeria. Our story, mission, vision and the core values behind every corridor we build.", about, "about.html")

# ---------------------------------------------------------------- SERVICES INDEX
life = [("route", "Design", "Corridor design, risk and vendor strategy.", "advisory"),
        ("search", "Source", "Vetted suppliers and binding landed-cost quotes.", "procurement"),
        ("car", "Import", "Vehicles and fleets from three continents.", "vehicle"),
        ("ship", "Move & Clear", "Sea, air and road freight with NCS brokerage.", "freight"),
        ("bolt", "Deliver", "Electric, GPS-tracked urban last-mile.", "last-mile")]
life_html = "".join(f'''<li class="reveal" style="--d:{i*0.08:.2f}s"><div class="icon-circle">{ic(icon)}</div><h3>{t}</h3><p>{d}</p><a href="{SVC[k]["file"]}">{SVC[k]["name"]}</a></li>''' for i, (icon, t, d, k) in enumerate(life))
rows = "".join(f'''<article class="svc-row reveal" id="{s["slug"]}" style="--svc-accent:{s["accent"]}">
      <div class="svc-row__media"><img src="images/{s["hero"]}" alt="" loading="lazy"><span class="svc-row__tag"><b>{s["num"]}</b> &nbsp;{s["name"]}</span></div>
      <div>
        <span class="svc-row__num">{s["num"]}</span>
        <h2>{s["name"]}</h2>
        <p class="tagline">{s["tagline"]}</p>
        <p>{s["short"]}</p>
        {bullets(s["bullets"][:4])}
        <div class="btn-row"><a class="btn btn--outline" href="{s["file"]}">Explore {s["name"]} {A}</a></div>
      </div>
    </article>''' for s in SERVICES)
services = f'''{page_hero("Our Services", "Five Service Lines. One Accountable Partner.", "Five integrated service lines spanning the entire international trade lifecycle, from vehicle importation to last-mile electric delivery, and from strategic procurement to freight corridors.", "containers.jpg", [(None, "Services")])}

<section class="section dark">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow eyebrow--center">The Trade Lifecycle</p>
      <h2>Covered End to End.</h2>
      <p class="lead">Use one service or all five. Either way, you have one contact and full accountability.</p>
    </div>
    <ol class="lifecycle" style="padding:0;margin:0">{life_html}</ol>
  </div>
</section>

<section class="section section--white">
  <div class="container svc-rows">
    {rows}
  </div>
</section>

{cta()}'''
page("services.html", "Services", "Vehicle logistics, electric last-mile delivery, procurement, freight & customs clearance, and supply chain advisory: five integrated service lines from VECTRA.", services, "services-index")

# ---------------------------------------------------------------- SERVICE DETAIL
for s in SERVICES:
    chips = "".join(f'<span class="chip">{ic(i)}{t}</span>' for i, t in s["chips"])
    hero_extra = f'''<div class="btn-row"><a class="btn btn--gold" href="contact.html?service={s["slug"]}">Request a Quote {A}</a><a class="btn btn--ghost" href="#process">How it works</a></div>
    <div class="svc-hero__meta">{chips}</div>'''
    hero = page_hero(f'Service {s["num"]}', s["name"], s["short"], s["hero"], [("services.html", "Services"), (None, s["name"])], hero_extra, "svc-hero")
    hero = hero.replace(f'<h1>{s["name"]}</h1>', f'<h1>{s["name"]}</h1>\n    <p class="tagline">{s["tagline"]}</p>')
    client_chips = "".join(f'<span class="chip">{ic(i)}{t}</span>' for i, t in s["clients"])
    breakdown = "".join(f'''<article class="breakdown__item reveal" style="--d:{i*0.08:.2f}s"><div class="icon-circle">{ic(icon)}</div><div><h3>{t}</h3><p>{d}</p></div></article>''' for i, (icon, t, d) in enumerate(s["breakdown"]))
    process = "".join(f'''<li class="reveal" style="--d:{i*0.07:.2f}s"><span class="process__step">Step {i+1:02d}</span><h3>{t}</h3><p>{d}</p></li>''' for i, (t, d) in enumerate(s["process"]))
    deliv = "".join(f'<li class="reveal">{ic("check")}<div><strong>{t}</strong><span>{d}</span></div></li>' for t, d in s["deliverables"])
    clients = "".join(f'<div class="client reveal" style="--d:{i*0.06:.2f}s"><div class="icon-circle">{ic(icon)}</div><strong>{t}</strong></div>' for i, (icon, t) in enumerate(s["clients"]))
    others = "".join(f'''<a class="other-svc" style="--svc-accent:{o["accent"]}" href="{o["file"]}"><span class="n">{o["num"]}</span><div class="row"><h3>{o["name"]}</h3>{ic("arrow")}</div></a>''' for o in SERVICES if o is not s)
    body = f'''{hero}

<section class="section section--white">
  <div class="container split" style="align-items:start">
    <div class="reveal">
      <p class="eyebrow">Overview</p>
      <h2>{s["tagline"]}</h2>
      <p class="lead" style="margin-top:24px">{s["intro"]}</p>
      <div class="gallery-strip" style="margin-top:36px;grid-template-columns:1fr">
        <figure><img src="images/{s["extra"]}" alt="" loading="lazy"></figure>
      </div>
    </div>
    <aside class="overview-card reveal" style="--d:.12s">
      <h3>What’s <span>included</span></h3>
      {bullets(s["bullets"])}
      <div class="overview-card__clients">
        <h4>Key clients</h4>
        <div class="chips">{client_chips}</div>
      </div>
      {MARK_BIG}
    </aside>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Service Breakdown</p>
      <h2>What We Deliver.</h2>
    </div>
    <div class="breakdown">{breakdown}</div>
  </div>
</section>

<section class="section dark" id="process">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Our Process</p>
      <h2>How It Works.</h2>
      <p class="lead">A clear, accountable sequence from first conversation to final delivery.</p>
    </div>
    <ol class="process" style="padding:0;margin:0">{process}</ol>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="split split--map" style="align-items:start">
      <div class="section-head reveal" style="margin:0">
        <p class="eyebrow">Key Deliverables</p>
        <h2>What You Receive.</h2>
        <p class="lead">Every engagement is documented, transparent and owned by one team.</p>
      </div>
      <ul class="deliverables deliverables--2" style="padding:0;margin:0">{deliv}</ul>
    </div>
  </div>
</section>

<section class="section section--cream section--tight">
  <div class="container">
    <div class="section-head reveal" style="margin-bottom:34px">
      <p class="eyebrow">Who We Serve</p>
      <h2>Built For.</h2>
    </div>
    <div class="clients">{clients}</div>
  </div>
</section>

{cta(title=f"Ready to Start With {s['name']}?", lead="Tell us what you need and a VECTRA specialist will come back with a tailored plan, timeline and itemised quote.", img=s["extra2"], service=s["slug"])}

<section class="section section--tight dark dark--deep">
  <div class="container">
    <div class="section-head reveal" style="margin-bottom:30px"><p class="eyebrow">Explore more</p><h2>Other Services.</h2></div>
    <div class="other-svcs">{others}</div>
  </div>
</section>'''
    page(s["file"], s["name"], f'{s["name"]} by VECTRA International Logistics: {s["short"]}', body, "services", s["accent"])

# ---------------------------------------------------------------- INDUSTRIES
ind_rows = "".join(f'''<article class="ind-row reveal">
      <div class="ind-row__media"><img src="images/{d["img"]}" alt="" loading="lazy"><span class="ind-row__num">0{i+1}</span></div>
      <div class="ind-row__body">
        <p class="eyebrow">Industry 0{i+1}</p>
        <h2>{d["name"]}</h2>
        <p class="ind-row__tag">{d["desc"]}</p>
        <p class="lead">{d["long"]}</p>
        <div class="ind-row__cols">
          <div><h4>What you need</h4>{bullets(d["needs"])}</div>
          <div><h4>How we serve you</h4><ul class="svc-links">{"".join(f'<li><a href="{SVC[k]["file"]}">{SVC[k]["name"]}{ic("arrow")}</a></li>' for k in d["svcs"])}</ul></div>
        </div>
      </div>
    </article>''' for i, d in enumerate(INDUSTRIES))
industries = f'''{page_hero("Target Markets", "Industries We Power.", "Tailored logistics and trade solutions for the sectors that move Nigeria’s economy.", "truck-road.jpg", [(None, "Industries")])}

<section class="section section--cream">
  <div class="container ind-rows">
    {ind_rows}
  </div>
</section>

{cta(title="Don’t See Your Sector?", lead="If your business moves goods across borders or across the city, we can design the corridor for it. Tell us what you need.")}'''
page("industries.html", "Industries", "VECTRA serves automotive & fleet, enterprise & industry, urban e-commerce, and government & NGO clients with tailored international logistics.", industries, "industries.html")

# ---------------------------------------------------------------- WHY
pillars = "".join(f'''<article class="pillar reveal">
      <span class="pillar__num">0{i+1}</span>
      <div><h3>{t}</h3><p>{d}</p></div>
      {bullets(b)}
    </article>''' for i, (icon, t, d, b) in enumerate(WHY))
cmp_rows = [("Scope", "Freight booking only", "End to end: procurement to final delivery"),
            ("Accountability", "Multiple hand-offs and contacts", "One contact, full accountability"),
            ("Network", "Booked capacity on third-party lanes", "Active corridors in the USA, Europe and Asia"),
            ("Nigerian clearance", "Outsourced, often reactive", "In-house NCS, FAAN and port expertise"),
            ("Error handling", "Fix problems after they occur", "Zero-margin protocol prevents failure"),
            ("Pricing", "Surprise charges at the terminal", "Itemised, binding quotes, no hidden fees")]
cmp_html = "".join(f'<tr><th scope="row">{a}</th><td class="muted">{b}</td><td class="v">{ic("check")}{c}</td></tr>' for a, b, c in cmp_rows)
why = f'''{page_hero("Why VECTRA", "More Than Freight. We Offer Architecture.", "VECTRA transforms volatile international trade lanes into highly predictable enterprise advantages.", "gwagon.jpg", [(None, "Why VECTRA")])}

<section class="section section--white">
  <div class="container reveal">
    <p class="statement">Where standard freight forwarders offer <em>transit</em>, VECTRA offers <em>architecture</em>.</p>
  </div>
</section>

<section class="section dark">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Our Advantage</p>
      <h2>Four Reasons Clients Choose VECTRA.</h2>
    </div>
    <div class="pillars">{pillars}</div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow eyebrow--center">The Difference</p>
      <h2>Transit vs. Architecture.</h2>
    </div>
    <div class="table-scroll reveal">
      <table class="compare">
        <thead><tr><th scope="col"><span class="sr-only">Criteria</span></th><th scope="col">Standard forwarder</th><th scope="col" class="v">VECTRA</th></tr></thead>
        <tbody>{cmp_html}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container split split--map">
    <div class="reveal">
      <p class="eyebrow">Global Corridors</p>
      <h2>Connecting Continents. Powering Nigeria.</h2>
      <p class="lead" style="margin:22px 0 28px">Active networks across the USA, Europe, and Asia, with true corridor ownership into Nigeria’s ports, airports and cities.</p>
      {bullets(["Origins: USA, UK, Germany, Japan, UAE, China, India", "Ports: Apapa, Tin Can, Onne", "Air: Lagos, Abuja, Kano", "Inland: Lagos, Abuja, Kano, Port Harcourt & ECOWAS routes"])}
    </div>
    <div class="reveal" style="--d:.15s">{corridor_map()}</div>
  </div>
</section>

{cta()}'''
page("why-vectra.html", "Why VECTRA", "3-continent reach, a zero-error standard, deep Nigerian market expertise and end-to-end ownership. Why clients choose VECTRA International Logistics.", why, "why-vectra.html")

# ---------------------------------------------------------------- CONTACT
svc_opts = "".join(f'''<div class="svc-option"><input type="checkbox" id="svc-{s["slug"]}" name="services" value="{s["slug"]}" data-label="{s["name"]}">
          <label for="svc-{s["slug"]}"><span class="icon-circle">{ic(s["icon"])}</span><span><strong>{s["name"]}</strong><small>{s["pick"]}</small></span><span class="tick">{ic("check")}</span></label></div>''' for s in SERVICES)
svc_opts += f'''<div class="svc-option"><input type="checkbox" id="svc-other" name="services" value="other" data-label="Not sure, please advise">
          <label for="svc-other"><span class="icon-circle">{ic("compass")}</span><span><strong>Not sure yet</strong><small>Tell us the problem and we’ll recommend the right mix.</small></span><span class="tick">{ic("check")}</span></label></div>'''

def opts(items):
    return '<option value="">Select…</option>' + "".join(f"<option>{i}</option>" for i in items)

contact = f'''{page_hero("Contact / Get a Quote", "Let’s Build Your Corridor.", "Tell us what you need to move, source or solve. A VECTRA specialist will come back to you with a tailored plan and quote.", "port-night.jpg", [(None, "Contact")])}

<section class="section section--cream">
  <div class="container contact-grid">
    <div class="form-card">
      <ol class="steps" aria-label="Enquiry progress">
        <li><b>Step 01</b>Services</li>
        <li><b>Step 02</b>Requirements</li>
        <li><b>Step 03</b>Contact details</li>
      </ol>
      <!-- To send enquiries to a form service (Formspree, Netlify Forms, a CRM), set data-endpoint to its URL.
           With data-endpoint empty, the form opens the visitor's email app addressed to data-mailto. -->
      <form id="quote-form" novalidate data-endpoint="" data-mailto="{EMAIL}">
        <div class="form-body">
          <fieldset class="form-step is-active" style="border:0;padding:0;margin:0">
            <legend class="sr-only">Service selection</legend>
            <h2>What can we help with?</h2>
            <p>Select every service that applies.</p>
            <div class="svc-select">{svc_opts}</div>
          </fieldset>

          <fieldset class="form-step" style="border:0;padding:0;margin:0">
            <legend class="sr-only">Cargo and business requirements</legend>
            <h2>Your requirements.</h2>
            <p>The more detail you share, the more precise our quote.</p>
            <div class="fields">
              <div class="field"><label for="cargo_type">Cargo / requirement type</label>
                <select id="cargo_type" name="cargo_type" required>{opts(["Vehicles", "General cargo", "Industrial equipment & machinery", "Construction materials", "Medical supplies", "Electronics", "Raw materials", "Parcels & documents (last-mile)", "Advisory / consulting", "Other"])}</select>
                <span class="err">Please choose a type.</span></div>
              <div class="field"><label for="origin">Origin</label>
                <select id="origin" name="origin" required>{opts(["United States", "United Kingdom", "Germany / rest of Europe", "China", "Japan", "India", "UAE", "Within Nigeria", "Other / not sure"])}</select>
                <span class="err">Please choose an origin.</span></div>
              <div class="field"><label for="destination">Destination city / state</label>
                <input id="destination" name="destination" type="text" placeholder="e.g. Abuja, FCT" required autocomplete="address-level2">
                <span class="err">Please enter a destination.</span></div>
              <div class="field"><label for="volume">Volume / quantity <span class="opt">(optional)</span></label>
                <input id="volume" name="volume" type="text" placeholder="e.g. 3 SUVs, 1×40ft FCL, 200 parcels/week"></div>
              <div class="field field--full"><span class="label" id="timeline-label">Timeline</span>
                <div class="radio-row" role="radiogroup" aria-labelledby="timeline-label">
                  <input type="radio" id="t1" name="timeline" value="Urgent (within 2 weeks)"><label for="t1">Urgent · within 2 weeks</label>
                  <input type="radio" id="t2" name="timeline" value="2–4 weeks" checked><label for="t2">2–4 weeks</label>
                  <input type="radio" id="t3" name="timeline" value="1–3 months"><label for="t3">1–3 months</label>
                  <input type="radio" id="t4" name="timeline" value="Planning ahead"><label for="t4">Planning ahead</label>
                </div></div>
              <div class="field field--full"><label for="details">Tell us more</label>
                <textarea id="details" name="details" placeholder="Make/model, specifications, HS codes, delivery windows, current challenges…" required></textarea>
                <span class="err">A short description helps us quote accurately.</span></div>
            </div>
          </fieldset>

          <fieldset class="form-step" style="border:0;padding:0;margin:0">
            <legend class="sr-only">Contact information</legend>
            <h2>How do we reach you?</h2>
            <p>A specialist will respond with a tailored plan and itemised quote.</p>
            <div class="fields">
              <div class="field"><label for="name">Full name</label><input id="name" name="name" type="text" required autocomplete="name"><span class="err">Please enter your name.</span></div>
              <div class="field"><label for="company">Company <span class="opt">(optional)</span></label><input id="company" name="company" type="text" autocomplete="organization"></div>
              <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"><span class="err">Please enter a valid email.</span></div>
              <div class="field"><label for="phone">Phone / WhatsApp</label><input id="phone" name="phone" type="tel" required autocomplete="tel" placeholder="+234"><span class="err">Please enter a phone number.</span></div>
              <div class="field field--full"><span class="label" id="method-label">Preferred contact method</span>
                <div class="radio-row" role="radiogroup" aria-labelledby="method-label">
                  <input type="radio" id="m1" name="contact_method" value="Email" checked><label for="m1">Email</label>
                  <input type="radio" id="m2" name="contact_method" value="Phone call"><label for="m2">Phone call</label>
                  <input type="radio" id="m3" name="contact_method" value="WhatsApp"><label for="m3">WhatsApp</label>
                </div></div>
              <div class="field field--full"><label class="consent"><input type="checkbox" name="consent" required> <span>I agree to VECTRA contacting me about this enquiry.</span></label><span class="err">Please confirm to continue.</span></div>
            </div>
            <div class="review"><strong style="display:block;margin-bottom:10px;color:var(--ink)">Your enquiry summary</strong><dl></dl></div>
          </fieldset>

          <p class="form-error" role="alert"></p>
          <div class="form-nav">
            <button type="button" class="btn btn--back" data-back hidden>{ic("arrow")} Back</button>
            <span></span>
            <button type="button" class="btn btn--gold" data-next>Continue {A}</button>
            <button type="submit" class="btn btn--gold" data-submit hidden>Submit Enquiry {A}</button>
          </div>
        </div>
      </form>
      <div class="form-success" role="status">
        <div class="icon-circle icon-circle--solid">{ic("check")}</div>
        <h2>Thank you, <span data-name></span>.</h2>
        <p>Your enquiry is on its way. A VECTRA specialist will review your requirements and come back to you with a tailored plan and quote.</p>
        <a class="btn btn--outline" href="services.html">Explore our services {A}</a>
      </div>
    </div>

    <aside class="contact-aside">
      <div class="aside-card">
        <h3>Talk to VECTRA</h3>
        <ul>
          <li><span class="icon-circle">{ic("pin")}</span><span><small>Headquarters</small>Abuja, FCT, Nigeria</span></li>
          <li><span class="icon-circle">{ic("mail")}</span><span><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
          <li><span class="icon-circle">{ic("phone")}</span><span><small>Phone</small><a href="tel:{PHONE_HREF}">{PHONE}</a></span></li>
          <li><span class="icon-circle">{ic("globe")}</span><span><small>Operational reach</small>United States · Europe · Asia</span></li>
        </ul>
      </div>
      <div class="next-steps">
        <h3>What happens next</h3>
        <ol>
          <li><div><strong>We review your brief</strong>A specialist studies your requirements and corridor.</div></li>
          <li><div><strong>You get a tailored plan</strong>Itemised costs, timelines and documentation needs.</div></li>
          <li><div><strong>We move</strong>One contact, from origin to final delivery.</div></li>
        </ol>
      </div>
    </aside>
  </div>
</section>'''
page("contact.html", "Contact & Get a Quote", "Request a quote from VECTRA International Logistics for vehicle logistics, electric last-mile, procurement, freight & customs or supply chain advisory.", contact, "contact.html")
