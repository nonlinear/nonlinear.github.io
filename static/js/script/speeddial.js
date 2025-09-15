// Custom drag for .cards a (Safari compatible)
document.addEventListener('DOMContentLoaded', () => {
	document.querySelectorAll('.cards a').forEach(card => {
		let isDragging = false;
		let startX = 0, startY = 0;
		let origX = 0, origY = 0;
		let dragElem;

		card.addEventListener('mousedown', function(e) {
			if (e.button !== 0) return; // Only left click
			isDragging = true;
			dragElem = card;
			startX = e.clientX;
			startY = e.clientY;
			origX = card.offsetLeft;
			origY = card.offsetTop;
			card.classList.add('dragging');
			card.style.transition = 'none';
			document.body.style.userSelect = 'none';
		});

		document.addEventListener('mousemove', function(e) {
			if (!isDragging || !dragElem) return;
			let dx = e.clientX - startX;
			let dy = e.clientY - startY;
			dragElem.style.transform = `translate(${dx}px, ${dy}px)`;
		});

		document.addEventListener('mouseup', function(e) {
			if (!isDragging || !dragElem) return;
			isDragging = false;
			dragElem.classList.remove('dragging');
			dragElem.style.transition = '';
			dragElem.style.transform = '';
			document.body.style.userSelect = '';
			dragElem = null;
		});
	});
});
