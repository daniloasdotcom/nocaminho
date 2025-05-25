// static/scroll-handler.js

document.addEventListener('DOMContentLoaded', () => {
    const scrollToFragment = (element) => {
        const offset = -50;
        const targetY = element.getBoundingClientRect().top + window.pageYOffset + offset;
        const startY = window.scrollY;
        const distance = targetY - startY;
        const duration = 1500;
        let startTime = null;

        const animateScroll = (currentTime) => {
            if (!startTime) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const progress = Math.min(timeElapsed / duration, 1);

            const ease = progress < 0.5
                ? 2 * progress * progress
                : -1 + (4 - 2 * progress) * progress;

            window.scrollTo(0, startY + distance * ease);

            if (timeElapsed < duration) {
                requestAnimationFrame(animateScroll);
            }
        };

        requestAnimationFrame(animateScroll);
    };

    document.querySelectorAll('button.down-arrow').forEach((btn, i) => {
        btn.setAttribute('data-target', 'block-' + (i + 1));
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const target = document.getElementById(targetId);

            document.querySelectorAll('button.down-arrow').forEach(b => b.classList.remove('active-arrow'));

            if (target) {
                target.classList.add('visible');

                const nextArrow = target.querySelector('button.down-arrow');
                if (nextArrow) {
                    nextArrow.classList.add('active-arrow');
                }

                scrollToFragment(target);
            }
        });
    });
});