const expandableCards = document.querySelectorAll('section .card');
const timelineItems = document.querySelectorAll('.timeline .item');

function closeExpandedCards() {
  expandableCards.forEach((card) => card.classList.remove('expanded'));
  timelineItems.forEach((item) => item.classList.remove('expanded'));
  document.body.classList.remove('card-expanded');
}

expandableCards.forEach((card) => {
  card.classList.add('expandable-card');

  card.addEventListener('click', () => {
    const isOpen = card.classList.contains('expanded');
    closeExpandedCards();

    if (!isOpen) {
      card.classList.add('expanded');
      document.body.classList.add('card-expanded');
    }
  });
});

timelineItems.forEach((item) => {
  item.addEventListener('click', () => {
    const isOpen = item.classList.contains('expanded');
    closeExpandedCards();

    if (!isOpen) {
      item.classList.add('expanded');
      document.body.classList.add('card-expanded');
    }
  });
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    closeExpandedCards();
  }
});
