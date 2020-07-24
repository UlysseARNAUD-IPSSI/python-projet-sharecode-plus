import View from "./View/index.js";
import saveCode from './misc/_saveCode.js';
import saveAndViewCode from './misc/_saveAndViewCode.js';
import view from './misc/_view.js';
import viewActivity from './misc/_view-activity.js';
import initializesCodeEditors from './misc/_initializesCodeEditors.js';
import modifierLangageDansEditor from "./misc/_modifierLangageDansEditor.js";


/*
 * Bootstrap
 */

window.editors = [];
window.viewActivity = viewActivity;
window.saveCode = saveCode;
window.saveAndViewCode = saveAndViewCode;
window.view = view;


/*
 * Main script
 */

window.addEventListener('popstate', function (event) {
    document.location.reload();
})

document.addEventListener('DOMContentLoaded', function () {
    initializesCodeEditors();
    if ('/' === window.location.pathname) loadHomeScript();
    if (/^\/edit\//.test(window.location.pathname)) loadEditScript();
});

function loadHomeScript() {
    const view = new View({
        url: '/_partials/last-added',
        urlChange: false,
        callback: function () {}
    });

    view.display();
}

function loadEditScript() {
    const languagesSelect = document.querySelector('select#language');
    languagesSelect.addEventListener('change', function changeLanguage(event) {
        const language = event.target.value;
        const codeSection = languagesSelect.closest('section#code');
        const {uid} = codeSection.dataset;
        modifierLangageDansEditor(uid, language);
    })
}

window.loadHomeScript = loadHomeScript;
window.loadEditScript = loadEditScript;