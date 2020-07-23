import contientEditor from "./_contientEditor.js";
import obtenirEditor from "./_obtenirEditor.js";

function saveCode(element) {

    const codeSection = element.closest('section#code');
    const {uid} = codeSection.dataset;

    if (contientEditor(uid)) {
        const editor = obtenirEditor(uid);
        const content = editor.editor.getValue();
        const language = editor.language || 'text';

        console.log({editor, uid, content, language});

        const formData = new FormData();
        formData.set('uid', uid);
        formData.set('content', content);
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