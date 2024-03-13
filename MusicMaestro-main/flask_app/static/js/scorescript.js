const tr = document.querySelector('#scoreboard');




tr.addEventListener('click', (event) => {
    if (event.target.tagName === 'BUTTON') {
        const button = event.target;
        const td = button.parentNode;
        const tr = td.parentNode;
        if (button.textContent === 'edit') {
            const span = td.firstElementChild;
            const input = document.createElement('input');
            input.type = 'text';
            input.value = span.textContent;
            td.insertBefore(input, span);
            td.removeChild(span);
            button.textContent = 'save';
        } else if (button.textContent === 'save') {
            const input = td.firstElementChild;
            const span = document.createElement('span');
            span.textContent = input.value;
            td.insertBefore(span, input);
            td.removeChild(input);
            button.textContent = 'edit';
        }
    }
});
