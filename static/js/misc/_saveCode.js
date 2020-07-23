import contientEditor from "./_contientEditor.js";
import obtenirEditor from "./_obtenirEditor.js";

function saveCode(element) {

    const codeSection = element.closest('section#code');
    const {uid} = codeSection.dataset;

    const form = codeSection.querySelector('form');

    if (contientEditor(uid)) {
        const editor = obtenirEditor(uid);
        const code = editor.editor.getValue();
        const language = editor.language || 'text';

        console.log({editor, uid, code, language});

        const formData = new FormData(form);
        formData.set('uid', uid);
        formData.set('code', code);
        formData.set('language', language);

        console.log({formData});

        fetch('/publish', {
            method: 'POST',
            body: formData
        }).then(function(response) {
            return response.text();
        }).then(function(response) {
            console.log({response});
        })
    }


}

export default saveCode;