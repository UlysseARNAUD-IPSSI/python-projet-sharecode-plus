import View from "../View/index.js";
import initializesCodeEditors from './_initializesCodeEditors.js';

function viewActivity(element) {

    const {id, mode} = element.dataset;

    const view = new View({
        url: '/' + mode + ('edit' === mode || 'view' === mode ? '/' + id : ''),
        urlChange: true,
        callback: function () {
            initializesCodeEditors();
        }
    });

    view.display();

}

export default viewActivity;