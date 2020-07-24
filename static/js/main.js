import View from "./View/index.js";
import saveCode from './misc/_saveCode.js';
import saveAndViewCode from './misc/_saveAndViewCode.js';
import view from './misc/_view.js';
import viewActivity from './misc/_view-activity.js';
import initializesCodeEditors from './misc/_initializesCodeEditors.js';
import modifierLangageDansEditor from "./misc/_modifierLangageDansEditor.js";
import obtenirEditor from "./misc/_obtenirEditor.js";


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
    initializesPage();
});

function loadHomeScript() {
    const view = new View({
        url: '/_partials/last-added',
        urlChange: false,
        callback: function () {
        }
    });

    view.display();
}

function loadEditScript() {
    const languagesSelect = document.querySelector('select#language');
    const codeSection = languagesSelect.closest('section#code');
    const {uid} = codeSection.dataset;
    languagesSelect.addEventListener('change', function changeLanguage(event) {
        const language = event.target.value;
        modifierLangageDansEditor(uid, language);
        const saveButton = document.querySelector('.toolbar a:first-child');
        saveButton.click();
        //window.location.reload(true);
        const currentSelected = languagesSelect.querySelector('option[selected]');
        if (currentSelected) currentSelected.removeAttribute('selected');
        languagesSelect.options[languagesSelect.selectedIndex].setAttribute('selected', true);
    });
    modifierLangageDansEditor(uid, languagesSelect.options[languagesSelect.selectedIndex].value);
}

function loadViewScript() {
    const codeSection = document.querySelector('section#code');
    const {uid} = codeSection.dataset;
    const editor = obtenirEditor(uid);
    console.log({editor});
    modifierLangageDansEditor(uid, editor.language);
}

function initializesPage() {
    initializesCodeEditors();
    if ('/' === window.location.pathname) loadHomeScript();
    if (/^\/edit\//.test(window.location.pathname)) loadEditScript();
    if (/^\/view\//.test(window.location.pathname)) loadViewScript();
}

window.initializesPage = initializesPage;