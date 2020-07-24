function modifierLangageDansEditor(uid, language) {
    for (
        let cursor = 0, cursorMax = editors.length;
        cursor < cursorMax;
        cursor++
    ) {
        const editor = editors[cursor];
        if (uid === editor.uid) {
            window.editors[cursor].language = language;
            const mode = CodeMirror.findModeByName(language);
            console.log({language, mode});
            let mime = 'text/plain';
            if (mode.mimes) mime = mode.mimes[0];
            else mime = mode.mime;
            window.editors[cursor].editor.setOption('mode', mime);
        }
    }
    return false;
}

export default modifierLangageDansEditor;