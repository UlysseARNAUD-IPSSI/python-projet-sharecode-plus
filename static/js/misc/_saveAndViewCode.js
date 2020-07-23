import contientEditor from "./_contientEditor.js";
import obtenirEditor from "./_obtenirEditor.js";

function saveAndViewCode(element) {

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
            return response.json();
        }).then(function(response) {
            if (response.ok) {
                view('/view/' + uid);
            }
        })
    }


}

export default saveAndViewCode;