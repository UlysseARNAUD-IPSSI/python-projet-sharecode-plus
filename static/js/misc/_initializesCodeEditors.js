import contientEditor from "./_contientEditor.js";
import enleverEditor from "./_enleverEditor.js";

function initializesCodeEditors() {

    const elements = document.querySelectorAll('.code-editor textarea');

    let languages = document.querySelector('input[name="mimes"]');

    if (languages) { // SI language ne vaut pas null ou undefined (en résumé: une valeur positive)
        languages.value = languages.value.replace(/'/g, '"');
        languages = JSON.parse(languages.value);
    }


    for (
        let cursor = 0, cursorMax = elements.length;
        cursor < cursorMax;
        cursor++
    ) {
        const element = elements[cursor];
        const codeSection = element.closest('section#code');

        const languagesSelect = codeSection.querySelector('select#language');
        let language;
        if (languagesSelect) {
            language = languagesSelect.options[languagesSelect.selectedIndex].value;
        }

        let {uid} = codeSection.dataset;

        /*if (undefined === language) {
            const defaultLanguage = 'Texte';
            codeSection.setAttribute('data-language', defaultLanguage);
            language = defaultLanguage;
        }*/

        const editor = CodeMirror.fromTextArea(element, {
            lineNumbers: true,
            mode: language ? languages[language] : 'text',
            theme: 'dracula'
        });

        if (true === contientEditor(uid)) {
            enleverEditor(uid);
        }

        let _editor = {uid, editor};
        if (language) _editor = {..._editor, language}
        editors.push(_editor);

    }

}

export default initializesCodeEditors;