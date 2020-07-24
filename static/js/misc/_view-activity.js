import View from "../View/index.js";
import initializesCodeEditors from './_initializesCodeEditors.js';

function viewActivity(element) {

    const {id, mode} = element.dataset;

    const url = '/' + mode + ('edit' === mode || 'view' === mode ? '/' + id : '');

    const view = new View({
        url,
        urlChange: true,
        callback: function (response) {
            console.log({response});
            const codeSection = response.querySelector('section#code');
            const {uid} = codeSection.dataset;
            if ('/create' === window.location.pathname) {
                history.replaceState({}, document.title, '/edit/' + uid);
            }
            initializesPage();
        }
    });

    view.display();

}

export default viewActivity;