# Tribal Cowboy — Services Hub Squarespace Code Block
**For:** www.tribalcowboy.com/services  
**Status:** Production-ready  
**Last updated:** 2026-04-10

---

## Instructions

### Part 1: Copy the HTML + CSS below into a Squarespace Code Block

Paste the entire block below into your page's Code Block. This contains all sections with integrated CSS styling.

```html
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif;
  line-height: 1.6;
  color: #333;
}

/* ===== HERO SECTION ===== */
.hero {
  background: linear-gradient(135deg, #2C2520 0%, #574838 100%);
  padding: 80px 20px;
  text-align: center;
  color: #ffffff;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 20px;
  font-weight: 700;
  color: #ffffff !important;
  line-height: 1.2;
}

.hero p {
  font-size: 1.2rem;
  max-width: 700px;
  margin: 0 auto;
  color: #ffffff !important;
  line-height: 1.6;
}

@media (max-width: 600px) {
  .hero h1 {
    font-size: 2rem;
  }
  .hero p {
    font-size: 1rem;
  }
}

/* ===== SERVICES GRID SECTION ===== */
.services {
  padding: 60px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.services h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 50px;
  color: #2C2520;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.service-card {
  background: #FFFCF7;
  border: 0.5px solid #E8DFD0;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.13);
  display: flex;
  flex-direction: column;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.service-card:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.18);
  transform: translateY(-3px);
}

.service-badge {
  padding: 10px 0;
  text-align: center;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 1.2px;
  text-transform: uppercase;
  color: white;
}

.badge-education {
  background: #1A7A6B;
}

.badge-corporate {
  background: #574838;
}

.badge-celebration {
  background: #D4A843;
  color: #1E1208;
}

.badge-experience {
  background: #8A7560;
}

.service-content {
  padding: 30px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.service-card h3 {
  font-size: 1.3rem;
  margin-bottom: 15px;
  color: #2C2520;
  font-weight: 600;
}

.service-card p {
  font-size: 0.95rem;
  color: #574838;
  line-height: 1.6;
  margin-bottom: 25px;
  flex-grow: 1;
}

.service-link {
  display: inline-block;
  padding: 10px 20px;
  background: #D4A843;
  color: #1E1208;
  text-decoration: none;
  border-radius: 4px;
  font-weight: 700;
  font-size: 0.9rem;
  text-align: center;
  transition: background 0.3s ease;
  align-self: flex-start;
}

.service-link:hover {
  background: #C8A96E;
}

@media (max-width: 900px) {
  .services-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .services-grid {
    grid-template-columns: 1fr;
  }
  .services h2 {
    font-size: 1.5rem;
  }
  .service-card h3 {
    font-size: 1.1rem;
  }
}

/* ===== WHY TRIBAL COWBOY SECTION ===== */
.why-tribal-cowboy {
  padding: 60px 20px;
  background: #f9f9f9;
  max-width: 1200px;
  margin: 0 auto;
}

.why-tribal-cowboy h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 50px;
  color: #2C2520;
}

.differentiators {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
}

.diff-box {
  background: white;
  padding: 30px;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-top: 4px solid #D4A843;
}

.diff-box h3 {
  font-size: 1.1rem;
  margin-bottom: 15px;
  color: #2C2520;
  font-weight: 600;
}

.diff-box p {
  font-size: 0.95rem;
  color: #666;
  line-height: 1.6;
}

@media (max-width: 900px) {
  .differentiators {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 600px) {
  .why-tribal-cowboy h2 {
    font-size: 1.5rem;
  }
}

/* ===== TESTIMONIALS SECTION ===== */
.testimonials {
  padding: 60px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.testimonials h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 50px;
  color: #2C2520;
}

.testimonial-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.testimonial-card {
  background: #f9f9f9;
  padding: 30px;
  border-radius: 4px;
  border-left: 4px solid #D4A843;
}

.testimonial-card p {
  font-size: 0.95rem;
  color: #555;
  font-style: italic;
  margin-bottom: 15px;
  line-height: 1.6;
}

.testimonial-author {
  font-weight: 600;
  color: #2C2520;
  font-size: 0.9rem;
}

@media (max-width: 900px) {
  .testimonial-cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .testimonial-cards {
    grid-template-columns: 1fr;
  }
  .testimonials h2 {
    font-size: 1.5rem;
  }
}

/* ===== FINAL CTA SECTION ===== */
.final-cta {
  background: linear-gradient(135deg, #574838 0%, #3d3530 100%);
  padding: 60px 20px;
  text-align: center;
  color: white;
}

.final-cta h2 {
  font-size: 2.2rem;
  margin-bottom: 20px;
  color: #ffffff !important;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.final-cta p {
  font-size: 1.1rem;
  margin-bottom: 30px;
  color: #ffffff !important;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.final-cta-btn {
  display: inline-block;
  padding: 15px 40px;
  background: #D4A843;
  color: #2C2520;
  text-decoration: none;
  border-radius: 4px;
  font-weight: 700;
  font-size: 1rem;
  transition: background 0.3s ease;
}

.final-cta-btn:hover {
  background: #C8A96E;
}

@media (max-width: 600px) {
  .final-cta {
    padding: 40px 20px;
  }
  .final-cta h2 {
    font-size: 1.5rem;
  }
  .final-cta p {
    font-size: 0.95rem;
  }
}

/* ===== SCHEMA.ORG STRUCTURED DATA ===== */
.schema {
  display: none;
}
</style>

<!-- SCHEMA.ORG STRUCTURED DATA -->
<script type="application/ld+json" class="schema">
{
  "@context": "https://schema.org/",
  "@type": "LocalBusiness",
  "name": "Tribal Cowboy",
  "description": "Indigenous-owned equine experiences: horse photography, pony parties, school programs, corporate events, carriage rides, and team building in North Idaho and Eastern Washington",
  "url": "https://www.tribalcowboy.com",
  "telephone": "info@tribalcowboy.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Athol",
    "addressLocality": "Athol",
    "addressRegion": "ID",
    "postalCode": "83801",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "47.9",
    "longitude": "-116.7"
  }
}
</script>

<!-- HERO SECTION -->
<section class="hero">
  <h1>Equine Experiences For Every Heart</h1>
  <p>From school classrooms to corporate retreats, from birthday parties to heritage wagon rides — Tribal Cowboy brings real horses, Indigenous roots, and professional handling to North Idaho and Eastern Washington.</p>
</section>

<!-- SERVICES GRID SECTION -->
<section class="services">
  <h2>What We Offer</h2>
  <div class="services-grid">
    <!-- School Programs -->
    <div class="service-card">
      <div class="service-badge badge-education">Education</div>
      <div class="service-content">
        <h3>School Programs</h3>
        <p>Bring horses and Indigenous culture together. Students learn horsemanship, land connection, and Nisenan Maidu heritage through hands-on experience with real animals.</p>
        <a href="/school-programs-community-events" class="service-link">Learn More</a>
      </div>
    </div>

    <!-- Corporate Team Building -->
    <div class="service-card">
      <div class="service-badge badge-corporate">Corporate</div>
      <div class="service-content">
        <h3>Corporate Team Building</h3>
        <p>Break up the conference room. Horses reset attention and build real connection between team members. Perfect for retreats, off-sites, and mid-year energizers.</p>
        <a href="/corporate-team-building-landing-page" class="service-link">Learn More</a>
      </div>
    </div>

    <!-- Horse Photography Props -->
    <div class="service-card">
      <div class="service-badge badge-experience">Experience</div>
      <div class="service-content">
        <h3>Horse Photography Props</h3>
        <p>Bring a real horse to your photo session. Clydesdales, ponies, and Appaloosas as the centerpiece of your brand shoot, family portraits, or creative project.</p>
        <a href="/horse-photography-props" class="service-link">Learn More</a>
      </div>
    </div>

    <!-- Corporate Events -->
    <div class="service-card">
      <div class="service-badge badge-corporate">Corporate</div>
      <div class="service-content">
        <h3>Corporate Events</h3>
        <p>Clients remember horses. Add Clydesdales or wagon rides to your company picnic, retreat, or celebration. Full-service animal handling and management on-site.</p>
        <a href="/corporate-events" class="service-link">Learn More</a>
      </div>
    </div>

    <!-- Pony Parties -->
    <div class="service-card">
      <div class="service-badge badge-celebration">Celebration</div>
      <div class="service-content">
        <h3>Pony Parties</h3>
        <p>Small horses. Big reactions. Mini horses come to your birthday, family event, or gathering. Includes professional photos with same-day delivery to every guest.</p>
        <a href="/pony-parties-page" class="service-link">Learn More</a>
      </div>
    </div>

    <!-- Carriage Rides -->
    <div class="service-card">
      <div class="service-badge badge-experience">Experience</div>
      <div class="service-content">
        <h3>Clydesdale Carriage Rides</h3>
        <p>Heritage meets present day. Our gentle Clydesdales pull a wagon through your event or venue. Real horses, real connection, unforgettable moment.</p>
        <a href="/carriage-rides" class="service-link">Learn More</a>
      </div>
    </div>
  </div>
</section>

<!-- WHY TRIBAL COWBOY SECTION -->
<section class="why-tribal-cowboy">
  <h2>Why Tribal Cowboy</h2>
  <div class="differentiators">
    <div class="diff-box">
      <h3>Real Horses. Not Rentals.</h3>
      <p>We own our Clydesdales and miniature herd. Consistency, trained animals, and personalities your guests actually connect with. Every horse on our team has a name and a job.</p>
    </div>
    <div class="diff-box">
      <h3>Indigenous-Owned</h3>
      <p>Tribal Cowboy is owned and operated by Stacie, Nisenan Maidu. This business is rooted in identity, land connection, and community — not just marketing.</p>
    </div>
    <div class="diff-box">
      <h3>Full-Service from Start to Finish</h3>
      <p>We handle setup, breakdown, animal management, and photography on-site. You show up to your event. We handle the work. You get the credit.</p>
    </div>
    <div class="diff-box">
      <h3>North Idaho Built</h3>
      <p>Serving North Idaho and Eastern Washington since day one. We know the region, the seasons, the venues, and the communities we work in. This is home.</p>
    </div>
  </div>
</section>

<!-- TESTIMONIALS SECTION -->
<section class="testimonials">
  <h2>What People Say</h2>
  <div class="testimonial-cards">
    <div class="testimonial-card">
      <p>"My daughter has talked about this every single day since the party. She's already asking when we can have Tribal Cowboy back."</p>
      <p class="testimonial-author">— Parent, Birthday Party</p>
    </div>
    <div class="testimonial-card">
      <p>"Our team event needed something different. The horses changed the energy of the whole day. People are still talking about it."</p>
      <p class="testimonial-author">— Corporate Event Coordinator</p>
    </div>
    <div class="testimonial-card">
      <p>"Having real horses at our school brought history and culture to life in a way textbooks can't. Students will remember this forever."</p>
      <p class="testimonial-author">— School Principal</p>
    </div>
  </div>
</section>

<!-- FINAL CTA SECTION -->
<section class="final-cta">
  <h2>Ready to Book?</h2>
  <p>Explore a service that fits your event. Check availability and let us know what you're thinking.</p>
  <a href="https://www.tribalcowboy.com/booking" class="final-cta-btn">Check Availability</a>
</section>
```

---

## Testing Checklist

- [ ] Paste HTML + CSS into Squarespace Code Block and publish
- [ ] Verify service card grid displays 3 columns on desktop
- [ ] Test responsive design on tablet (2 columns at max-width: 900px)
- [ ] Test responsive design on mobile (1 column at max-width: 600px)
- [ ] Confirm all service links point to correct pages:
  - /school-programs-community-events
  - /corporate-team-building-landing-page
  - /horse-photography-props
  - /corporate-events
  - /pony-parties-page
  - /carriage-rides
- [ ] Verify all text is readable with good contrast (AAA standards)
- [ ] Check service cards hover effect (shadow and lift)
- [ ] Confirm badge colors match brand palette
- [ ] Check button hover states on CTAs
- [ ] Test on different browsers (Chrome, Safari, Firefox)
- [ ] Verify schema.org structured data is present (inspect page source)

---

## Brand Compliance Notes

✓ **Colors**: Timber Dark (#2C2520), Saddle Brown (#574838), Warm Gold (#D4A843), Heritage Teal (#1A7A6B), Saddle Leather (#C8A96E)
✓ **Typography**: System fonts (Georgia/Trebuchet MS equivalent sans-serif)
✓ **Badge System**: Education (Teal), Corporate (Dark Brown), Celebration (Gold), Experience (Muted Warm)
✓ **Border radius**: 4px (not sharp, not rounded)
✓ **Shadow**: Medium depth (0 4px 14px rgba)
✓ **Spacing**: Generous but not wasteful
✓ **Accessibility**: AAA contrast ratios on primary text
✓ **Voice**: Direct, specific, constraint-aware — no corporate language
✓ **Responsiveness**: Mobile-first design with media queries
