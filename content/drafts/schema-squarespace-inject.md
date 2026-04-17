# Schema Markup — Squarespace Code Injection
*Paste this into: Settings > Advanced > Code Injection > Header*
*This tells Google and AI engines that Tribal Cowboy is a real, structured local business.*

---

## How to add in Squarespace
1. Go to **Settings** (left sidebar)
2. Click **Advanced**
3. Click **Code Injection**
4. Paste the entire code block below into the **Header** field
5. Click **Save**

---

## The Code (paste everything between the triple-backtick lines)

```html
<!-- Tribal Cowboy — Structured Data Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      "@id": "https://www.tribalcowboy.com/#business",
      "name": "Tribal Cowboy LLC",
      "alternateName": "Tribal Cowboy",
      "description": "Indigenous-owned equine experience company offering pony rides, Clydesdale carriage rides, wagon rides, horse photo sessions, and school programs across North Idaho and Eastern Washington. Owned and led by Stacie Huffhines, Nisenan Maidu.",
      "url": "https://www.tribalcowboy.com",
      "logo": "https://www.tribalcowboy.com/logo.png",
      "image": "https://www.tribalcowboy.com/og-image.jpg",
      "telephone": "",
      "email": "info@tribalcowboy.com",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Athol",
        "addressRegion": "ID",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "47.9574",
        "longitude": "-116.7007"
      },
      "areaServed": [
        "Athol, ID",
        "Coeur d'Alene, ID",
        "Hayden, ID",
        "Spirit Lake, ID",
        "Rathdrum, ID",
        "Post Falls, ID",
        "Spokane, WA",
        "Spokane Valley, WA",
        "North Idaho",
        "Eastern Washington"
      ],
      "priceRange": "$$",
      "currenciesAccepted": "USD",
      "openingHours": "Mo-Su 08:00-20:00",
      "sameAs": [
        "https://www.instagram.com/tribalcowboy",
        "https://www.facebook.com/TribalCowboys"
      ],
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Tribal Cowboy Services",
        "itemListElement": [
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Pony Visits",
              "description": "Ponies for birthday parties, school visits, and community events. Children and adults can meet, groom, and learn about ponies up close."
            },
            "priceSpecification": {
              "@type": "PriceSpecification",
              "price": "300",
              "priceCurrency": "USD",
              "description": "Starting price for 2 hours"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Pony-Driven Wagon Rides",
              "description": "Cozy wagons pulled by ponies, seating up to four. Perfect for neighborhood gatherings, school visits, and family fun."
            },
            "priceSpecification": {
              "@type": "PriceSpecification",
              "price": "550",
              "priceCurrency": "USD",
              "description": "Starting price for 2 hours"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Clydesdale Carriage Experience",
              "description": "Clydesdales pulling a full-size carriage at festivals, fundraisers, and parades. These horses weigh over 1,800 pounds."
            },
            "priceSpecification": {
              "@type": "PriceSpecification",
              "price": "800",
              "priceCurrency": "USD",
              "description": "Starting price for 1.5–2 hours"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Horse Photography Sessions",
              "description": "Horses and decorated wagons as live props for professional photo sessions. On-site animal management included."
            },
            "priceSpecification": {
              "@type": "PriceSpecification",
              "price": "250",
              "priceCurrency": "USD",
              "description": "Starting price for 1 hour"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Educational School Programs",
              "description": "Horses brought to schools and community centers for hands-on educational visits. Stacie teaches the history of horses in the Pacific Northwest alongside real horsemanship."
            }
          }
        ]
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How much do pony rides cost in North Idaho?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pony visits start at $300 for 2 hours. Pony-drawn wagon rides start at $550 for 2 hours. Additional time is available. Tribal Cowboy serves North Idaho and Eastern Washington."
          }
        },
        {
          "@type": "Question",
          "name": "What areas does Tribal Cowboy serve?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tribal Cowboy is based in Athol, Idaho and serves North Idaho and Eastern Washington — including Coeur d'Alene, Hayden, Spirit Lake, Rathdrum, Post Falls, Spokane, and Spokane Valley. Travel fees may apply for locations outside this area."
          }
        },
        {
          "@type": "Question",
          "name": "Are pony rides safe for toddlers?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Our ponies are trained for events with young children. A handler walks with every rider. We do not leave a child unattended on an animal. Children who can sit upright independently — typically 2 years and older — can ride with a handler walking alongside."
          }
        },
        {
          "@type": "Question",
          "name": "How much space is needed for pony rides?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Plan for roughly 30 feet of open space in any direction — enough room for the pony to walk a circle comfortably. For wagon rides, a wider path and clearance for turning is needed. Grass and packed dirt are ideal surfaces."
          }
        },
        {
          "@type": "Question",
          "name": "How far in advance should I book Tribal Cowboy?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Spring and summer dates fill 4–8 weeks out. For large events or school programs, book as early as possible. Check availability at tribalcowboy.as.me or email info@tribalcowboy.com."
          }
        },
        {
          "@type": "Question",
          "name": "Does Tribal Cowboy travel to Spokane?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Tribal Cowboy regularly serves Spokane and Spokane Valley. Travel fees may apply. Contact info@tribalcowboy.com with your event details for a quote."
          }
        },
        {
          "@type": "Question",
          "name": "Can I hire Tribal Cowboy for a school visit?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Tribal Cowboy brings horses to schools, community centers, libraries, and tribal programs for hands-on educational visits. Programs can align with curriculum goals or run as open experiential time with the animals. Contact info@tribalcowboy.com."
          }
        },
        {
          "@type": "Question",
          "name": "What is the horse photography experience?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Tribal Cowboy brings horses and decorated wagons to your location as live props for a professional photo session. You or your photographer shoot — they handle the animals. Clydesdale photo sessions start at $250 for 1 hour in North Idaho and Eastern Washington."
          }
        },
        {
          "@type": "Question",
          "name": "What surfaces work for pony rides?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Grass and packed dirt are ideal. Gravel works. Pavement is fine for short visits. Bare asphalt in heat is not suitable — it's hard on hooves."
          }
        },
        {
          "@type": "Question",
          "name": "Is Tribal Cowboy Indigenous-owned?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Tribal Cowboy is owned and led by Stacie Huffhines, Nisenan Maidu. The business is based in Athol, Idaho and serves North Idaho and Eastern Washington."
          }
        }
      ]
    }
  ]
}
</script>
```

---

## Notes
- Replace `"telephone": ""` with your phone number if you want it publicly indexed
- Replace `/logo.png` and `/og-image.jpg` with your actual Squarespace image URLs (right-click any image on your site → Copy Image Address)
- The FAQPage schema feeds directly into Google's FAQ rich results AND AI answer engines — this is what makes you show up in "pony rides Idaho" type queries
