function shareOn(platform) {
  const text = document.getElementById('output').innerText;
  const encodedText = encodeURIComponent(text);
  const url = encodeURIComponent(window.location.href);
  let shareUrl = "";

  switch (platform) {
    case 'twitter':
      shareUrl = `https://twitter.com/intent/tweet?text=${encodedText}&url=${url}`;
      break;
    case 'facebook':
      shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}&quote=${encodedText}`;
      break;
    case 'whatsapp':
      shareUrl = `https://api.whatsapp.com/send?text=${encodedText}%20${url}`;
      break;
    case 'linkedin':
      shareUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${url}&title=${encodedText}`;
      break;
  }
  if (shareUrl) {
    window.open(shareUrl, '_blank');
  }
}

['twitter', 'facebook', 'whatsapp', 'linkedin'].forEach(id => {
  const btn = document.getElementById(`shareBtn-${id}`);
  if (btn) {
    btn.addEventListener('click', () => shareOn(id));
  }
});

document.getElementById('generateBtn').addEventListener('click', () => {
  const input = document.getElementById('input').value.trim();
  if (!input) {
    alert('Veuillez saisir un sujet.');
    return;
  }
  // Simuler génération de post (à remplacer par appel réel IA)
  const generated = `Voici un post généré sur : "${input}"\n#Buzz #AI #SocialMedia`;
  document.getElementById('output').innerText = generated;
});

document.getElementById('copyBtn').addEventListener('click', () => {
  const output = document.getElementById('output').innerText;
  if (!output) {
    alert('Aucun texte à copier.');
    return;
  }
  navigator.clipboard.writeText(output).then(() => {
    alert('Texte copié dans le presse-papiers !');
  });
});
