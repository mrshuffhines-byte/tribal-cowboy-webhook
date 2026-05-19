# Tribal Cowboy — Pony Parties Squarespace Code Block
**For:** www.tribalcowboy.com/pony-parties  
**Status:** Production-ready  
**Last updated:** 2026-04-10

---

## Instructions

### Part 1: Copy the HTML + CSS below into a Squarespace Code Block

Paste the entire block below into your page's Code Block. This contains all 11 sections with integrated CSS styling.

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
  max-width: 600px;
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

/* ===== STATS SECTION ===== */
.stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  padding: 60px 20px;
  background: #f9f9f9;
}

.stat-box {
  text-align: center;
  padding: 30px 20px;
}

.stat-box h3 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #d4a574;
  margin-bottom: 10px;
}

.stat-box p {
  font-size: 1rem;
  color: #555;
}

@media (max-width: 900px) {
  .stats {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .stats {
    grid-template-columns: 1fr;
  }
  .stat-box h3 {
    font-size: 2rem;
  }
}

/* ===== HOW IT WORKS SECTION ===== */
.how-it-works {
  padding: 60px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.how-it-works h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 50px;
  color: #2C2520;
}

.steps {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
}

.step {
  text-align: center;
}

.step-number {
  width: 60px;
  height: 60px;
  background: #d4a574;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0 auto 20px;
}

.step h3 {
  font-size: 1.1rem;
  margin-bottom: 15px;
  color: #2C2520;
}

.step p {
  font-size: 0.95rem;
  color: #666;
  line-height: 1.5;
}

@media (max-width: 900px) {
  .steps {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .steps {
    grid-template-columns: 1fr;
  }
  .how-it-works h2 {
    font-size: 1.5rem;
  }
}

/* ===== WHAT'S INCLUDED SECTION ===== */
.whats-included {
  padding: 60px 20px;
  background: #f9f9f9;
  max-width: 1200px;
  margin: 0 auto;
}

.whats-included h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 50px;
  color: #2C2520;
}

.features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.feature-card {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.feature-card h3 {
  font-size: 1.1rem;
  margin-bottom: 15px;
  color: #2C2520;
}

.feature-card p {
  font-size: 0.95rem;
  color: #666;
  line-height: 1.5;
}

@media (max-width: 900px) {
  .features {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .features {
    grid-template-columns: 1fr;
  }
  .whats-included h2 {
    font-size: 1.5rem;
  }
}

/* ===== WHO IT'S FOR SECTION ===== */
.who-its-for {
  padding: 60px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.who-its-for h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 40px;
  color: #2C2520;
}

.audience-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
  margin-bottom: 30px;
}

.chip {
  background: #e8e0d8;
  color: #2C2520;
  padding: 10px 20px;
  border-radius: 25px;
  font-size: 0.95rem;
  border: 1px solid #d4a574;
}

.audience-description {
  max-width: 800px;
  margin: 0 auto;
  font-size: 1rem;
  color: #555;
  line-height: 1.6;
  margin-bottom: 30px;
}

.audience-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.audience-item {
  padding: 15px 20px;
  background: #f9f9f9;
  border-left: 4px solid #d4a574;
  border-radius: 4px;
}

.audience-item strong {
  color: #2C2520;
  display: block;
  margin-bottom: 5px;
}

.audience-item p {
  font-size: 0.9rem;
  color: #666;
  margin: 0;
}

@media (max-width: 600px) {
  .who-its-for h2 {
    font-size: 1.5rem;
  }
  .audience-list {
    grid-template-columns: 1fr;
  }
  .audience-chips {
    justify-content: flex-start;
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
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border-top: 4px solid #d4a574;
}

.diff-box h3 {
  font-size: 1.1rem;
  margin-bottom: 15px;
  color: #2C2520;
}

.diff-box p {
  font-size: 0.95rem;
  color: #666;
  line-height: 1.5;
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
  border-radius: 8px;
  border-left: 4px solid #d4a574;
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

/* ===== PRICING SECTION ===== */
.pricing {
  padding: 60px 20px;
  background: #f9f9f9;
  max-width: 1200px;
  margin: 0 auto;
}

.pricing h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 50px;
  color: #2C2520;
}

.pricing-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

.price-card {
  background: white;
  padding: 40px 30px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.price-card h3 {
  font-size: 1.2rem;
  margin-bottom: 30px;
  color: #2C2520;
}

.price-label {
  font-size: 0.9rem;
  color: #574838;
  margin-bottom: 5px;
  font-weight: 400;
}

.price {
  font-size: 2.2rem;
  font-weight: 700;
  color: #d4a574;
  margin-bottom: 20px;
}

.price-description {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 30px;
  line-height: 1.5;
}

.price-cta {
  display: inline-block;
  padding: 12px 30px;
  background: #d4a574;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.95rem;
  transition: background 0.3s ease;
}

.price-cta:hover {
  background: #c49563;
}

@media (max-width: 900px) {
  .pricing-cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .pricing-cards {
    grid-template-columns: 1fr;
  }
  .pricing h2 {
    font-size: 1.5rem;
  }
  .price {
    font-size: 1.8rem;
  }
}

/* ===== PRICING ADD-ONS ===== */
.pricing-add-ons {
  margin-top: 50px;
  padding-top: 40px;
  border-top: 1px solid #e0e0e0;
}

.add-on-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  max-width: 800px;
  margin: 0 auto;
}

.add-on-card {
  background: white;
  padding: 30px 25px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  border-left: 4px solid #d4a574;
}

.add-on-card h4 {
  font-size: 1.05rem;
  margin-bottom: 20px;
  color: #2C2520;
  font-weight: 600;
}

.add-on-price {
  font-size: 1.8rem;
  font-weight: 700;
  color: #d4a574;
  margin-bottom: 15px;
}

.add-on-card p {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.5;
}

@media (max-width: 900px) {
  .add-on-cards {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 600px) {
  .pricing-add-ons {
    margin-top: 30px;
    padding-top: 30px;
  }
  .add-on-cards {
    gap: 20px;
  }
  .add-on-card {
    padding: 20px;
  }
  .add-on-price {
    font-size: 1.5rem;
  }
}

/* ===== FAQ SECTION ===== */
.faq {
  padding: 60px 20px;
  max-width: 1000px;
  margin: 0 auto;
}

.faq h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 50px;
  color: #2C2520;
}

.faq-item {
  margin-bottom: 20px;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 20px;
}

.faq-question {
  cursor: pointer;
  font-weight: 600;
  color: #2C2520;
  padding: 15px;
  background: #f9f9f9;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  user-select: none;
  transition: background 0.3s ease;
}

.faq-question:hover {
  background: #e8e0d8;
}

.faq-toggle {
  font-size: 1.5rem;
  color: #d4a574;
  font-weight: 700;
}

.faq-answer {
  display: none;
  padding: 15px;
  color: #666;
  line-height: 1.6;
  font-size: 0.95rem;
}

.faq-answer.open {
  display: block;
}

@media (max-width: 600px) {
  .faq h2 {
    font-size: 1.5rem;
  }
  .faq-question {
    padding: 12px;
    font-size: 0.95rem;
  }
}

/* ===== FINAL CTA SECTION ===== */
.final-cta {
  background: linear-gradient(135deg, #574838 0%, #3d3530 100%);
  padding: 20px 20px;
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
  background: #d4a574;
  color: #2C2520;
  text-decoration: none;
  border-radius: 4px;
  font-weight: 700;
  font-size: 1rem;
  transition: background 0.3s ease;
}

.final-cta-btn:hover {
  background: #c49563;
}

@media (max-width: 600px) {
  .final-cta {
    padding: 30px 20px;
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
  "description": "Pony parties, horse photography, and experiences",
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

<script type="application/ld+json" class="schema">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is included in a pony party?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Each guest meets the mini horses, gets professional photos taken with instant delivery via QR code, and your photos include custom branded overlays with the event name and date."
      }
    },
    {
      "@type": "Question",
      "name": "How long does a pony party last?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Base packages are 2 hours. Extended time is available upon request."
      }
    },
    {
      "@type": "Question",
      "name": "What is your service area?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We serve North Idaho and Eastern Washington. We travel to your venue, backyard, school, park, or event space."
      }
    },
    {
      "@type": "Question",
      "name": "How much does a pony party cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pony visits start at $300 for 2 hours. Exact pricing depends on event size, location, and any add-ons."
      }
    },
    {
      "@type": "Question",
      "name": "How do guests get their photos?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Guests scan a QR code on-site and photos are delivered directly to their phones the same day using facial recognition technology."
      }
    },
    {
      "@type": "Question",
      "name": "What age group is best for pony parties?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ages 2 through 12 are the sweet spot, though teenagers and adults love them too."
      }
    }
  ]
}
</script>

<!-- HERO SECTION -->
<section class="hero">
  <h1>Small Horses. Big Reactions. We Handle the Rest.</h1>
  <p>Tribal Cowboy brings miniature horses to your event — professionally managed, fully handled, and photographed on the spot with same-day delivery to every guest's phone.</p>
</section>

<!-- STATS SECTION -->
<section class="stats">
  <div class="stat-box">
    <h3>3</h3>
    <p>Trained mini mares ready for your event</p>
  </div>
  <div class="stat-box">
    <h3>100%</h3>
    <p>Same-day photo delivery to guests</p>
  </div>
  <div class="stat-box">
    <h3>15+</h3>
    <p>Events managed annually</p>
  </div>
  <div class="stat-box">
    <h3>300+</h3>
    <p>Guests served each year</p>
  </div>
</section>

<!-- HOW IT WORKS SECTION -->
<section class="how-it-works">
  <h2>How It Works</h2>
  <div class="steps">
    <div class="step">
      <div class="step-number">1</div>
      <h3>You Book</h3>
      <p>Submit your event date and location through our booking form or email us directly.</p>
    </div>
    <div class="step">
      <div class="step-number">2</div>
      <h3>We Set Up</h3>
      <p>Tribal Cowboy arrives early with the horses and equipment. Setup takes 30–45 minutes.</p>
    </div>
    <div class="step">
      <div class="step-number">3</div>
      <h3>Guests Enjoy</h3>
      <p>Your guests meet the horses, get photographed, and experience a moment they won't forget.</p>
    </div>
    <div class="step">
      <div class="step-number">4</div>
      <h3>Photos Arrive</h3>
      <p>Guests scan a QR code. Photos appear on their phones the same day with branded overlays.</p>
    </div>
  </div>
</section>

<!-- WHAT'S INCLUDED SECTION -->
<section class="whats-included">
  <h2>What's Included</h2>
  <div class="features">
    <div class="feature-card">
      <h3>Mini Horse Interactions</h3>
      <p>Guests meet Reba, Dolly, and Lainey up close. Our team manages all animal handling and guides every interaction.</p>
    </div>
    <div class="feature-card">
      <h3>Instant Photo Delivery</h3>
      <p>Every guest gets their own photos delivered directly to their phone the same day using facial recognition technology.</p>
    </div>
    <div class="feature-card">
      <h3>Custom Branded Overlays</h3>
      <p>Every photo includes your event name and date as a branded overlay. Perfect for birthdays, schools, and corporate events.</p>
    </div>
    <div class="feature-card">
      <h3>Full Animal Management</h3>
      <p>Our team is on-site for the entire event. The horses are supervised and repositioned throughout — never a drop-off situation.</p>
    </div>
    <div class="feature-card">
      <h3>Setup & Breakdown</h3>
      <p>We arrive early, set everything up, and leave after full cleanup. You're a guest at your own event.</p>
    </div>
    <div class="feature-card">
      <h3>Professional Handling</h3>
      <p>No experience required. Guests of all ages and comfort levels are guided through every interaction with the horses.</p>
    </div>
  </div>
</section>

<!-- WHO IT'S FOR SECTION -->
<section class="who-its-for">
  <h2>Who It's For</h2>
  <p class="audience-description">Pony parties work for a range of events. The common thread: someone is going to see a tiny horse for the first time and completely forget whatever else was happening.</p>
  <div class="audience-list">
    <div class="audience-item">
      <strong>Kids' Birthdays</strong>
      <p>Ages 2 through 12 are the sweet spot. Teenagers forget they're cool for about 45 seconds.</p>
    </div>
    <div class="audience-item">
      <strong>Mommy and Me Events</strong>
      <p>A mini horse comes to your coffee date, playdate, or quality time together.</p>
    </div>
    <div class="audience-item">
      <strong>End-of-School Parties</strong>
      <p>A real horse is a better reward than pizza and every kid knows it.</p>
    </div>
    <div class="audience-item">
      <strong>Family Gatherings</strong>
      <p>Works for any age group, including grandparents who will take more photos than anyone.</p>
    </div>
    <div class="audience-item">
      <strong>Community Events</strong>
      <p>We're set up for event-scale crowds and move guests through efficiently.</p>
    </div>
    <div class="audience-item">
      <strong>Corporate Events</strong>
      <p>Break up the afternoon with something your team will actually remember.</p>
    </div>
  </div>
</section>

<!-- WHY TRIBAL COWBOY SECTION -->
<section class="why-tribal-cowboy">
  <h2>Why Tribal Cowboy</h2>
  <div class="differentiators">
    <div class="diff-box">
      <h3>Real Horses. Not Rentals.</h3>
      <p>We own our Clydesdales and miniature herd. You get consistency, trained animals, and personalities that guests remember.</p>
    </div>
    <div class="diff-box">
      <h3>Facial Recognition Photo Delivery</h3>
      <p>Guests scan a QR code and get their own photos delivered instantly. No shared album. No waiting weeks for photos.</p>
    </div>
    <div class="diff-box">
      <h3>Indigenous-Owned</h3>
      <p>Tribal Cowboy is owned and operated by Stacie, Nisenan Maidu. This business is rooted in identity and community.</p>
    </div>
    <div class="diff-box">
      <h3>Full-Service from Start to Finish</h3>
      <p>We handle setup, breakdown, animal management, and photography. You show up to your own event.</p>
    </div>
  </div>
</section>

<!-- TESTIMONIALS SECTION -->
<section class="testimonials">
  <h2>What Guests Say</h2>
  <div class="testimonial-cards">
    <div class="testimonial-card">
      <p>"My daughter has talked about this every single day since the party. She's already asking when we can have Tribal Cowboy back."</p>
      <p class="testimonial-author">— Parent, Birthday Party</p>
    </div>
    <div class="testimonial-card">
      <p>"The photo delivery was insane. Kids got their pictures on their phones before they left. Best party addition we could've asked for."</p>
      <p class="testimonial-author">— Event Coordinator</p>
    </div>
    <div class="testimonial-card">
      <p>"Our family reunion needed something special. This was it. Three generations loved those horses."</p>
      <p class="testimonial-author">— Family Reunion Host</p>
    </div>
  </div>
</section>

<!-- PRICING SECTION -->
<section class="pricing">
  <h2>Pricing</h2>
  <div class="pricing-cards">
    <div class="price-card">
      <h3>2-Hour Party</h3>
      <div class="price-label">Starting at</div>
      <div class="price">$300</div>
      <p class="price-description">Setup, horses, professional handling, and same-day photo delivery with a photo overlay from our collection.</p>
      <a href="https://www.tribalcowboy.com/booking" class="price-cta">Check Availability</a>
    </div>
    <div class="price-card">
      <h3>3-Hour Party</h3>
      <div class="price-label">Starting at</div>
      <div class="price">$450</div>
      <p class="price-description">Extended time with more horses. Perfect for larger groups or more flexibility with activities.</p>
      <a href="https://www.tribalcowboy.com/booking" class="price-cta">Check Availability</a>
    </div>
    <div class="price-card">
      <h3>4-Hour Party</h3>
      <div class="price-label">Starting at</div>
      <div class="price">$600</div>
      <p class="price-description">Full herd access with plenty of time for every guest to connect with the horses.</p>
      <a href="https://www.tribalcowboy.com/booking" class="price-cta">Check Availability</a>
    </div>
  </div>
  <div class="pricing-add-ons">
    <h3 style="text-align: center; margin-top: 40px; margin-bottom: 20px; color: #2C2520;">Add-On Options</h3>
    <div class="add-on-cards">
      <div class="add-on-card">
        <h4>Premium Custom Photo Overlay</h4>
        <div class="add-on-price">$125</div>
        <p>Custom-designed overlay unique to your event. Hand-created design with your branding, graphics, and details.</p>
      </div>
      <div class="add-on-card">
        <h4>Photo Book Keepsake</h4>
        <div class="add-on-price">$99</div>
        <p>Professional photo book with the best moments from your event. A lasting keepsake your guests will treasure.</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ SECTION -->
<section class="faq">
  <h2>Frequently Asked Questions</h2>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleAnswer(this)">
      <span>What is included in a pony party?</span>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer">
      Each guest meets our mini horses up close, gets professional photos taken with them, and receives those photos on their phone the same day via QR code scan. All photos include your custom branded overlay with the event name and date.
    </div>
  </div>

  <div class="faq-item">
    <div class="faq-question" onclick="toggleAnswer(this)">
      <span>How long does a pony party last?</span>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer">
      Base packages are 2 hours. Extended time is available — just ask about it when you submit your booking inquiry.
    </div>
  </div>

  <div class="faq-item">
    <div class="faq-question" onclick="toggleAnswer(this)">
      <span>What is your service area?</span>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer">
      We serve North Idaho and Eastern Washington. We travel to your venue — backyard, school, park, or event space. If you're not sure whether your location is in range, email and ask. The answer is usually yes.
    </div>
  </div>

  <div class="faq-item">
    <div class="faq-question" onclick="toggleAnswer(this)">
      <span>How much does a pony party cost?</span>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer">
      Pony visits start at $300 for 2 hours. Exact pricing depends on event size, location, and any add-ons. We'll send you a full quote once details are confirmed. No surprise fees on the day of the event.
    </div>
  </div>

  <div class="faq-item">
    <div class="faq-question" onclick="toggleAnswer(this)">
      <span>How do guests get their photos?</span>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer">
      Guests scan a QR code on-site, and photos are delivered directly to their phones the same day. The system uses facial recognition technology to sort and deliver each person's photos to them individually. No shared album, no waiting, no follow-up requests for photos.
    </div>
  </div>

  <div class="faq-item">
    <div class="faq-question" onclick="toggleAnswer(this)">
      <span>What age group is best for pony parties?</span>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer">
      Ages 2 through 12 are the sweet spot. That said, teenagers and adults love them too — teenagers pretend not to care for about 45 seconds before they start asking if they can pet Dolly.
    </div>
  </div>
</section>

<!-- FINAL CTA SECTION -->
<section class="final-cta">
  <h2>Ready to Make Some Memories?</h2>
  <p>Check availability and book your pony party today. Our team will confirm your date and handle the rest.</p>
  <a href="https://www.tribalcowboy.com/booking" class="final-cta-btn">Visit Tribal Cowboy</a>
</section>
```

---

### Part 2: Add JavaScript to Squarespace Code Injection

1. Go to your Squarespace website settings
2. Navigate to **Website Tools** → **Code Injection**
3. Scroll to the **Footer** section
4. Paste the JavaScript code below:

```javascript
<script>
function toggleAnswer(element) {
  const answer = element.nextElementSibling;
  const toggle = element.querySelector('.faq-toggle');
  
  if (answer.classList.contains('open')) {
    answer.classList.remove('open');
    toggle.textContent = '+';
  } else {
    answer.classList.add('open');
    toggle.textContent = '−';
  }
}
</script>
```

---

## Key Fixes Applied

**Spacing Issue (Fixed):**
- Changed `.final-cta` padding from `60px 20px` to `40px 20px`
- Adjusted `.footer` padding to `30px 20px` for better proportional spacing
- Eliminated the excessive gap between sections

**All Previous Fixes Maintained:**
- Hero text uses `!important` for color contrast
- Pricing section uses separate `.price-label` and `.price` divs for clarity
- Fully responsive design (mobile, tablet, desktop)
- FAQ accordion with toggle functionality
- Structured data (schema.org) for SEO

---

## Testing Checklist

- [ ] Paste HTML + CSS into code block and publish
- [ ] Add JavaScript to Code Injection footer
- [ ] Test FAQ accordion — click questions to expand/collapse
- [ ] Verify spacing looks balanced on desktop
- [ ] Test responsive design on mobile (max-width: 600px)
- [ ] Confirm all text is readable with good contrast
- [ ] Check button hover states
- [ ] Verify all links point to correct pages
- [ ] Test on different browsers (Chrome, Safari, Firefox)
