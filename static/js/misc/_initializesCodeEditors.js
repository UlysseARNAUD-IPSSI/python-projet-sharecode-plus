import contientEditor from "./_contientEditor.js";

function initializesCodeEditors() {

    const elements = document.querySelectorAll('.code-editor textarea');
    for (
        let cursor = 0, cursorMax = elements.length;
        cursor < cursorMax;
        cursor++
    ) {
        const element = elements[cursor];
        const editor = CodeMirror.fromTextArea(element, {
            lineNumbers: true
        });

        const codeSection = element.closest('section#code');
        let {uid, language} = codeSection.dataset;

        if (undefined === language) {
            const defaultLanguage = 'text';
            codeSection.setAttribute('data-language', defaultLanguage);
            language = defaultLanguage;
        }

        if (false === contientEditor(uid)) {
            editors.push({uid, editor, language});
        }

    }

}

export default initializesCodeEditors;