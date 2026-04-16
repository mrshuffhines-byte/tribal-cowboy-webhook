# Horse Photography Props — Squarespace Code Block
**For:** www.tribalcowboy.com/horse-photography-props  
**Status:** Updated with dropdown FAQ + conditional photo delivery answer  
**Last updated:** 2026-04-10

---

## Changes Made

✓ Fixed font visibility in features section (background #3D3530, text explicitly #F3EDE3)
✓ Converted FAQ to interactive dropdown/accordion (click to expand/collapse)
✓ Updated "How do we get our photos?" to be conditional on event size + always mention link access
✓ Removed duplicate CSS rules

---

<div id="tc-hp-wrap">
  <style>
    #tc-hp-wrap {
      font-family: 'Trebuchet MS', sans-serif;
      color: #2C2520;
      background: #FFFCF7;
    }
    #tc-hp-wrap * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    .tc-hp-hero {
      background: linear-gradient(135deg, #2C2520 0%, #3D3530 100%);
      color: #F3EDE3;
      padding: 80px 40px !important;
      text-align: center;
      border: 3px solid #D4A843 !important;
      border-radius: 8px !important;
      margin-bottom: 60px !important;
    }
    .tc-hp-hero h1 {
      font-family: 'Georgia', serif !important;
      font-size: 48px !important;
      font-weight: bold !important;
      margin-bottom: 20px !important;
      color: #D4A843 !important;
      line-height: 1.2 !important;
    }
    .tc-hp-hero p {
      font-size: 18px !important;
      margin-bottom: 30px !important;
      line-height: 1.6 !important;
      color: #F3EDE3 !important;
    }
    .tc-hp-cta-btn {
      background: #D4A843 !important;
      color: #2C2520 !important;
      padding: 14px 28px !important;
      border: none !important;
      border-radius: 4px !important;
      font-size: 16px !important;
      font-weight: bold !important;
      cursor: pointer !important;
      text-decoration: none !important;
      display: inline-block !important;
      transition: all 0.3s ease !important;
    }
    .tc-hp-cta-btn:hover {
      background: #F3EDE3 !important;
      color: #2C2520 !important;
    }
    .tc-hp-stats {
      background: #3D3530 !important;
      color: #F3EDE3 !important;
      padding: 40px 20px !important;
      margin-bottom: 60px !important;
      border-radius: 8px !important;
      display: flex !important;
      flex-wrap: wrap !important;
      justify-content: space-around !important;
      gap: 20px !important;
    }
    .tc-hp-stat {
      text-align: center !important;
      flex: 1 1 200px !important;
      min-width: 150px !important;
    }
    .tc-hp-stat .number {
      font-family: 'Georgia', serif !important;
      font-size: 36px !important;
      font-weight: bold !important;
      color: #D4A843 !important;
    }
    .tc-hp-stat .label {
      font-size: 14px !important;
      margin-top: 8px !important;
      color: #F3EDE3 !important;
    }
    .tc-hp-section {
      margin-bottom: 60px !important;
    }
    .tc-hp-section h2 {
      font-family: 'Georgia', serif !important;
      font-size: 32px !important;
      margin-bottom: 30px !important;
      text-align: center !important;
      color: #2C2520 !important;
    }
    .tc-hp-section h3 {
      font-family: 'Georgia', serif !important;
      font-size: 24px !important;
      color: #2C2520 !important;
      margin-bottom: 15px !important;
    }
    .tc-hp-cards {
      display: flex !important;
      flex-wrap: wrap !important;
      gap: 20px !important;
      margin-bottom: 40px !important;
    }
    .tc-hp-card {
      flex: 1 1 250px !important;
      background: #F3EDE3 !important;
      padding: 20px !important;
      border-radius: 6px !important;
      border-left: 4px solid #D4A843 !important;
      min-height: 200px !important;
      display: flex !important;
      flex-direction: column !important;
    }
    .tc-hp-card h4 {
      font-family: 'Georgia', serif !important;
      font-size: 18px !important;
      color: #2C2520 !important;
      margin-bottom: 12px !important;
    }
    .tc-hp-card p {
      font-size: 14px !important;
      line-height: 1.5 !important;
      color: #574838 !important;
    }
    .tc-hp-process {
      display: flex !important;
      flex-wrap: wrap !important;
      justify-content: space-between !important;
      gap: 30px !important;
      margin-bottom: 40px !important;
    }
    .tc-hp-step {
      flex: 1 1 150px !important;
      text-align: center !important;
      min-width: 140px !important;
    }
    .tc-hp-step .step-num {
      background: #D4A843 !important;
      color: #2C2520 !important;
      width: 50px !important;
      height: 50px !important;
      border-radius: 50% !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      font-size: 20px !important;
      font-weight: bold !important;
      margin: 0 auto 15px auto !important;
    }
    .tc-hp-step p {
      font-size: 14px !important;
      line-height: 1.4 !important;
      color: #574838 !important;
    }
    .tc-hp-features {
      background: #3D3530 !important;
      color: #F3EDE3 !important;
      padding: 40px !important;
      border-radius: 8px !important;
      margin-bottom: 40px !important;
    }
    .tc-hp-features h3 {
      color: #D4A843 !important;
      margin-bottom: 25px !important;
    }
    .tc-hp-feature-item {
      display: flex !important;
      gap: 15px !important;
      margin-bottom: 18px !important;
      padding-bottom: 15px !important;
      border-bottom: 1px solid #574838 !important;
    }
    .tc-hp-feature-item:last-child {
      border-bottom: none !important;
      margin-bottom: 0 !important;
    }
    .tc-hp-feature-item::before {
      content: "✓" !important;
      color: #D4A843 !important;
      font-weight: bold !important;
      font-size: 18px !important;
      min-width: 20px !important;
    }
    .tc-hp-feature-item p {
      font-size: 14px !important;
      line-height: 1.5 !important;
      color: #F3EDE3 !important;
    }
    .tc-hp-pricing {
      display: flex !important;
      flex-wrap: wrap !important;
      gap: 20px !important;
      margin-bottom: 40px !important;
    }
    .tc-hp-price-card {
      flex: 1 1 250px !important;
      border: 2px solid #D4A843 !important;
      border-radius: 6px !important;
      padding: 30px !important;
      text-align: center !important;
      background: #F3EDE3 !important;
      position: relative !important;
    }
    .tc-hp-price-badge {
      position: absolute !important;
      top: -12px !important;
      left: 50% !important;
      transform: translateX(-50%) !important;
      background: #D4A843 !important;
      color: #2C2520 !important;
      padding: 4px 12px !important;
      border-radius: 20px !important;
      font-size: 12px !important;
      font-weight: bold !important;
    }
    .tc-hp-price-card h4 {
      font-family: 'Georgia', serif !important;
      font-size: 22px !important;
      color: #2C2520 !important;
      margin: 15px 0 20px 0 !important;
    }
    .tc-hp-price {
      font-family: 'Georgia', serif !important;
      font-size: 28px !important;
      color: #D4A843 !important;
      margin-bottom: 20px !important;
      font-weight: bold !important;
    }
    .tc-hp-price-list {
      text-align: left !important;
      margin-bottom: 25px !important;
    }
    .tc-hp-price-list li {
      list-style: none !important;
      font-size: 13px !important;
      color: #574838 !important;
      padding: 8px 0 !important;
      border-bottom: 1px solid #E8DFD5 !important;
    }
    .tc-hp-price-list li:last-child {
      border-bottom: none !important;
    }
    .tc-hp-btn {
      background: #2C2520 !important;
      color: #F3EDE3 !important;
      padding: 12px 24px !important;
      border: none !important;
      border-radius: 4px !important;
      font-size: 14px !important;
      font-weight: bold !important;
      cursor: pointer !important;
      text-decoration: none !important;
      display: inline-block !important;
      transition: all 0.3s ease !important;
      width: 100% !important;
    }
    .tc-hp-btn:hover {
      background: #D4A843 !important;
      color: #2C2520 !important;
    }
    .tc-hp-testimonials {
      margin-bottom: 40px !important;
    }
    .tc-hp-testimonial-cards {
      display: flex !important;
      flex-wrap: wrap !important;
      gap: 20px !important;
    }
    .tc-hp-testimonial {
      flex: 1 1 280px !important;
      background: #F3EDE3 !important;
      padding: 25px !important;
      border-radius: 6px !important;
      border-left: 4px solid #D4A843 !important;
    }
    .tc-hp-testimonial-quote {
      font-style: italic !important;
      color: #574838 !important;
      font-size: 14px !important;
      line-height: 1.6 !important;
      margin-bottom: 15px !important;
      position: relative !important;
    }
    .tc-hp-testimonial-quote::before {
      content: '"' !important;
      font-size: 40px !important;
      color: #D4A843 !important;
      position: absolute !important;
      top: -10px !important;
      left: 0 !important;
    }
    .tc-hp-testimonial-author {
      font-weight: bold !important;
      color: #2C2520 !important;
      font-size: 13px !important;
    }
    /* FAQ ACCORDION STYLES */
    .tc-hp-faq {
      margin-bottom: 40px !important;
    }
    .tc-hp-faq-item {
      background: #F3EDE3 !important;
      margin-bottom: 12px !important;
      border-radius: 6px !important;
      border-left: 4px solid #D4A843 !important;
      overflow: hidden !important;
    }
    .tc-hp-faq-question {
      padding: 20px !important;
      cursor: pointer !important;
      display: flex !important;
      justify-content: space-between !important;
      align-items: center !important;
      background: #F3EDE3 !important;
      transition: background 0.3s ease !important;
      user-select: none !important;
    }
    .tc-hp-faq-question:hover {
      background: #EFE8DC !important;
    }
    .tc-hp-faq-question h4 {
      font-family: 'Georgia', serif !important;
      color: #2C2520 !important;
      font-size: 16px !important;
      margin: 0 !important;
      flex-grow: 1 !important;
    }
    .tc-hp-faq-toggle {
      color: #D4A843 !important;
      font-size: 20px !important;
      font-weight: bold !important;
      margin-left: 15px !important;
      transition: transform 0.3s ease !important;
      min-width: 20px !important;
      text-align: center !important;
    }
    .tc-hp-faq-item.active .tc-hp-faq-toggle {
      transform: rotate(180deg) !important;
    }
    .tc-hp-faq-answer {
      max-height: 0 !important;
      overflow: hidden !important;
      transition: max-height 0.3s ease, padding 0.3s ease !important;
    }
    .tc-hp-faq-item.active .tc-hp-faq-answer {
      max-height: 500px !important;
      padding: 0 20px 20px 20px !important;
    }
    .tc-hp-faq-answer p {
      color: #574838 !important;
      font-size: 14px !important;
      line-height: 1.5 !important;
      margin: 0 !important;
    }
    .tc-hp-footer-cta {
      background: linear-gradient(135deg, #2C2520 0%, #3D3530 100%);
      color: #F3EDE3 !important;
      padding: 50px 40px !important;
      border: 3px solid #D4A843 !important;
      border-radius: 8px !important;
      text-align: center !important;
      margin-bottom: 40px !important;
    }
    .tc-hp-footer-cta h2 {
      font-family: 'Georgia', serif !important;
      font-size: 32px !important;
      color: #D4A843 !important;
      margin-bottom: 20px !important;
    }
    .tc-hp-footer-cta p {
      font-size: 16px !important;
      margin-bottom: 25px !important;
    }
    .tc-hp-footer-info {
      background: #F3EDE3 !important;
      padding: 30px !important;
      border-radius: 6px !important;
      text-align: center !important;
      display: flex !important;
      flex-wrap: wrap !important;
      justify-content: space-around !important;
      gap: 20px !important;
    }
    .tc-hp-footer-info-block {
      flex: 1 1 200px !important;
    }
    .tc-hp-footer-info-block strong {
      display: block !important;
      color: #2C2520 !important;
      margin-bottom: 5px !important;
    }
    .tc-hp-footer-info-block p {
      color: #574838 !important;
      font-size: 14px !important;
    }
    @media (max-width: 768px) {
      .tc-hp-hero {
        padding: 50px 25px !important;
      }
      .tc-hp-hero h1 {
        font-size: 32px !important;
      }
      .tc-hp-hero p {
        font-size: 16px !important;
      }
      .tc-hp-cards {
        flex-direction: column !important;
      }
      .tc-hp-card {
        flex: 1 1 100% !important;
      }
      .tc-hp-process {
        flex-direction: column !important;
      }
      .tc-hp-pricing {
        flex-direction: column !important;
      }
      .tc-hp-testimonial-cards {
        flex-direction: column !important;
      }
      .tc-hp-footer-info {
        flex-direction: column !important;
      }
    }
    @media (max-width: 600px) {
      .tc-hp-hero {
        padding: 40px 15px !important;
      }
      .tc-hp-hero h1 {
        font-size: 24px !important;
      }
      .tc-hp-section h2 {
        font-size: 24px !important;
      }
      .tc-hp-stats {
        flex-direction: column !important;
        padding: 30px 15px !important;
      }
      .tc-hp-cta-btn {
        width: 100% !important;
      }
      .tc-hp-faq-question {
        flex-direction: column !important;
        align-items: flex-start !important;
      }
      .tc-hp-faq-toggle {
        margin-left: 0 !important;
        margin-top: 10px !important;
      }
    }
  </style>
  <div class="tc-hp-hero">
    <h1>Horse Photography Props</h1>
    <p>Real horses. Real moments. Instant delivery.</p>
    <button class="tc-hp-cta-btn">Check Availability</button>
  </div>
  <div class="tc-hp-stats">
    <div class="tc-hp-stat">
      <div class="number">1,800 lbs</div>
      <div class="label">Of pure Clydesdale</div>
    </div>
    <div class="tc-hp-stat">
      <div class="number">Instant</div>
      <div class="label">Photo Delivery via QR</div>
    </div>
    <div class="tc-hp-stat">
      <div class="number">Custom</div>
      <div class="label">Branded Overlays</div>
    </div>
    <div class="tc-hp-stat">
      <div class="number">We Travel</div>
      <div class="label">North Idaho & EWA</div>
    </div>
  </div>
  <div class="tc-hp-section">
    <h2>How It Works</h2>
    <div class="tc-hp-process">
      <div class="tc-hp-step">
        <div class="step-num">1</div>
        <p>Book your session</p>
      </div>
      <div class="tc-hp-step">
        <div class="step-num">2</div>
        <p>We arrive with horses</p>
      </div>
      <div class="tc-hp-step">
        <div class="step-num">3</div>
        <p>You pose & shoot</p>
      </div>
      <div class="tc-hp-step">
        <div class="step-num">4</div>
        <p>Scan QR for photos</p>
      </div>
      <div class="tc-hp-step">
        <div class="step-num">5</div>
        <p>Download instantly</p>
      </div>
    </div>
  </div>
  <div class="tc-hp-section">
    <h2>What You Get</h2>
    <div class="tc-hp-cards">
      <div class="tc-hp-card">
        <h4>The Horses</h4>
        <p>Working with Millie and Abby, our Clydesdales. They're calm, patient, and naturally photogenic.</p>
      </div>
      <div class="tc-hp-card">
        <h4>Custom Branded Overlays</h4>
        <p>Every photo gets your name, date, or logo. It's all in the file — no editing required.</p>
      </div>
      <div class="tc-hp-card">
        <h4>Professional Coaching</h4>
        <p>We guide poses, timing, and angles so you get the shots you actually want.</p>
      </div>
      <div class="tc-hp-card">
        <h4>Same-Day Delivery</h4>
        <p>Scan a QR code, get your full gallery. Print, share, or download — your choice.</p>
      </div>
      <div class="tc-hp-card">
        <h4>Flexible Backgrounds</h4>
        <p>Barn, pasture, trees, or open field. Pick the setting that matches your vision.</p>
      </div>
      <div class="tc-hp-card">
        <h4>Licensed & Insured</h4>
        <p>We handle all safety and liability. You focus on the moment.</p>
      </div>
    </div>
  </div>
  <div class="tc-hp-features">
    <h3>Why Book With Us</h3>
    <div class="tc-hp-feature-item">
      <p><strong>Real Clydesdales, not rentals.</strong> Our horses live here. They know the land and the work.</p>
    </div>
    <div class="tc-hp-feature-item">
      <p><strong>Indigenous-owned business.</strong> Stacie is Nisenan Maidu, rooting this work in authentic community connection.</p>
    </div>
    <div class="tc-hp-feature-item">
      <p><strong>No hidden fees.</strong> What you book is what you pay. Travel included for North Idaho & EWA.</p>
    </div>
    <div class="tc-hp-feature-item">
      <p><strong>Instant photos in your pocket.</strong> QR code scanning means no waiting for galleries or edits.</p>
    </div>
    <div class="tc-hp-feature-item">
      <p><strong>We show up prepared.</strong> Grooming, setup, safety checks — we handle the details.</p>
    </div>
  </div>
  <div class="tc-hp-section">
    <h2>Pricing</h2>
    <div class="tc-hp-pricing">
      <div class="tc-hp-price-card">
        <div class="tc-hp-price-badge">Standard</div>
        <h4>Single Horse Session</h4>
        <div class="tc-hp-price">$350</div>
        <ul class="tc-hp-price-list">
          <li>1 hour session</li>
          <li>1 Clydesdale</li>
          <li>20-30 photos</li>
          <li>Custom overlay</li>
          <li>Same-day delivery</li>
        </ul>
        <button class="tc-hp-btn">Book Now</button>
      </div>
      <div class="tc-hp-price-card">
        <div class="tc-hp-price-badge" style="background: #D4A843 !important;">Most Popular</div>
        <h4>Dual Horse Session</h4>
        <div class="tc-hp-price">$550</div>
        <ul class="tc-hp-price-list">
          <li>1.5 hour session</li>
          <li>2 Clydesdales</li>
          <li>40-50 photos</li>
          <li>Custom overlay</li>
          <li>Same-day delivery</li>
        </ul>
        <button class="tc-hp-btn">Book Now</button>
      </div>
      <div class="tc-hp-price-card">
        <div class="tc-hp-price-badge" style="background: #1A7A6B !important;">Extended</div>
        <h4>Premium Full Session</h4>
        <div class="tc-hp-price">$750</div>
        <ul class="tc-hp-price-list">
          <li>2 hour session</li>
          <li>2+ Clydesdales & ponies</li>
          <li>75-100 photos</li>
          <li>Custom overlay</li>
          <li>Location change included</li>
          <li>Same-day delivery</li>
        </ul>
        <button class="tc-hp-btn">Book Now</button>
      </div>
    </div>
  </div>
  <div class="tc-hp-testimonials">
    <h2>From Our Sessions</h2>
    <div class="tc-hp-testimonial-cards">
      <div class="tc-hp-testimonial">
        <div class="tc-hp-testimonial-quote">We got our photos instantly. The kids still talk about meeting Millie.</div>
        <div class="tc-hp-testimonial-author">— Jennifer & Family, Post Falls</div>
      </div>
      <div class="tc-hp-testimonial">
        <div class="tc-hp-testimonial-quote">Professional quality without the wait. That's what sold us.</div>
        <div class="tc-hp-testimonial-author">— Marcus, Corporate Event Coordinator</div>
      </div>
      <div class="tc-hp-testimonial">
        <div class="tc-hp-testimonial-quote">Best engagement photos we've ever done. Real animals, real moment.</div>
        <div class="tc-hp-testimonial-author">— Sarah & David, Engaged Couple</div>
      </div>
    </div>
  </div>
  <div class="tc-hp-faq">
    <h2>Questions?</h2>
    <div class="tc-hp-faq-item">
      <div class="tc-hp-faq-question">
        <h4>How long is a typical session?</h4>
        <span class="tc-hp-faq-toggle">+</span>
      </div>
      <div class="tc-hp-faq-answer">
        <p>Sessions run 1–2 hours depending on package. We include travel, setup, and coaching time. No rushed photos.</p>
      </div>
    </div>
    <div class="tc-hp-faq-item">
      <div class="tc-hp-faq-question">
        <h4>Do you travel outside Athol?</h4>
        <span class="tc-hp-faq-toggle">+</span>
      </div>
      <div class="tc-hp-faq-answer">
        <p>Yes. We service North Idaho and Eastern Washington. Travel is included in all packages.</p>
      </div>
    </div>
    <div class="tc-hp-faq-item">
      <div class="tc-hp-faq-question">
        <h4>What if the weather is bad?</h4>
        <span class="tc-hp-faq-toggle">+</span>
      </div>
      <div class="tc-hp-faq-answer">
        <p>Rain doesn't scare us or the horses. We'll reschedule if conditions are genuinely unsafe for animals or people.</p>
      </div>
    </div>
    <div class="tc-hp-faq-item">
      <div class="tc-hp-faq-question">
        <h4>Can we choose our location?</h4>
        <span class="tc-hp-faq-toggle">+</span>
      </div>
      <div class="tc-hp-faq-answer">
        <p>Absolutely. Bring us to your property, a park, or a scenic spot. We'll set up where you want to shoot.</p>
      </div>
    </div>
    <div class="tc-hp-faq-item">
      <div class="tc-hp-faq-question">
        <h4>How do we get our photos?</h4>
        <span class="tc-hp-faq-toggle">+</span>
      </div>
      <div class="tc-hp-faq-answer">
        <p><strong>For larger events with multiple people:</strong> We provide a QR code that guests scan to access a shared gallery link. Everyone gets instant access to download the photos they want.</p>
        <p style="margin-top: 10px !important;"><strong>For private sessions:</strong> You'll receive a personal link to your gallery where you can browse and download all your photos. Both ways, you get that link instantly — no waiting for edits or uploads on our end.</p>
      </div>
    </div>
    <div class="tc-hp-faq-item">
      <div class="tc-hp-faq-question">
        <h4>Can we edit or request shots?</h4>
        <span class="tc-hp-faq-toggle">+</span>
      </div>
      <div class="tc-hp-faq-answer">
        <p>The gallery is yours to work with. You choose which photos to download. Custom edits available for additional fee.</p>
      </div>
    </div>
  </div>
  <div class="tc-hp-footer-cta">
    <h2>Ready to Shoot?</h2>
    <p>Book your session now. Limited dates — check availability.</p>
    <button class="tc-hp-cta-btn">Check Availability</button>
  </div>
  <div class="tc-hp-footer-info">
    <div class="tc-hp-footer-info-block">
      <strong>Check Availability</strong>
      <p><a href="https://www.tribalcowboy.com" style="color: #D4A843; text-decoration: none;">www.tribalcowboy.com</a></p>
    </div>
    <div class="tc-hp-footer-info-block">
      <strong>Email</strong>
      <p><a href="mailto:info@tribalcowboy.com" style="color: #D4A843; text-decoration: none;">info@tribalcowboy.com</a></p>
    </div>
    <div class="tc-hp-footer-info-block">
      <strong>Follow</strong>
      <p><a href="https://www.instagram.com/tribalcowboy" style="color: #D4A843; text-decoration: none;">@TribalCowboy</a></p>
    </div>
  </div>
  <script>
    document.querySelectorAll('.tc-hp-faq-question').forEach(question => {
      question.addEventListener('click', function() {
        const faqItem = this.parentElement;
        faqItem.classList.toggle('active');
      });
    });
  </script>
</div>

---

## Installation Instructions

1. Copy the entire HTML + CSS + JavaScript block above (starting with `<div id="tc-hp-wrap">`)
2. Paste into a Squarespace Code Block on your Horse Photography Props page
3. Test the FAQ dropdowns by clicking each question
4. Verify the features section text is readable (dark background #3D3530 with light text)
5. Test on mobile to confirm responsive behavior

## What's Changed

**✓ Font Visibility Fix:**
- `.tc-hp-features` background: `#2C2520` → `#3D3530` (lighter dark brown for better contrast)
- `.tc-hp-feature-item p`: Added explicit `color: #F3EDE3 !important;` for text visibility

**✓ FAQ Dropdown Functionality:**
- Changed static Q&A to interactive accordion
- Click any question to expand/collapse the answer
- Plus sign (+) rotates when expanded
- Smooth CSS transitions for expand/collapse

**✓ Updated Photo Delivery Answer:**
- Now conditional: explains two delivery methods based on event size
- **Larger events:** QR code for shared gallery access
- **Private sessions:** Personal link to individual gallery
- Both methods always result in getting a link — emphasizes instant access

**✓ Removed Duplicate CSS Rules:**
- Cleaned up duplicate `.tc-hp-features` and `.tc-hp-feature-item p` definitions

## Testing Checklist

- [ ] Paste code into Squarespace Code Block and publish
- [ ] Click each FAQ question to confirm dropdown opens/closes smoothly
- [ ] Verify features section text (#F3EDE3) is readable on dark background (#3D3530)
- [ ] Test on mobile (768px and 600px breakpoints)
- [ ] Confirm "How do we get our photos?" shows both delivery methods clearly
- [ ] Check all buttons are clickable and hover properly
- [ ] Verify all links work (booking, email, Instagram)
