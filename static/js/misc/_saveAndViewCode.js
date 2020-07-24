import contientEditor from "./_contientEditor.js";
import obtenirEditor from "./_obtenirEditor.js";

function saveAndViewCode(element) {

    const codeSection = element.closest('section#code');
    const {uid} = codeSection.dataset;

    const languagesSelect = codeSection.querySelector('select#language');

    if (contientEditor(uid)) {
        const editor = obtenirEditor(uid);
        const content = editor.editor.getValue();
        const language = languagesSelect.options[languagesSelect.selectedIndex].value;

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
            return response.json();
        }).then(function(response) {
            if (response.ok) {
                view('/view/' + uid);
            }
        })
    }


}

export default saveAndViewCode;