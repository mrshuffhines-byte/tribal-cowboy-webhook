(function() {
  const styles = {
    heading: {},
    body: {},
    colors: new Set()
  };

  const h1 = document.querySelector('h1');
  if (h1) {
    const s = window.getComputedStyle(h1);
    styles.heading.fontFamily = s.fontFamily;
    styles.heading.fontSize = s.fontSize;
    styles.heading.color = s.color;
  }

  const p = document.querySelector('p');
  if (p) {
    const s = window.getComputedStyle(p);
    styles.body.fontFamily = s.fontFamily;
    styles.body.fontSize = s.fontSize;
    styles.body.color = s.color;
  }

  // Sample some colors
  document.querySelectorAll('h1, h2, p, a, button, div').forEach(el => {
    const s = window.getComputedStyle(el);
    if (s.backgroundColor && s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.backgroundColor !== 'transparent') {
      styles.colors.add(s.backgroundColor);
    }
    if (s.color) {
      styles.colors.add(s.color);
    }
  });

  return {
    typography: styles.heading.fontFamily ? styles : "Could not determine",
    colors: Array.from(styles.colors).slice(0, 10)
  };
})();