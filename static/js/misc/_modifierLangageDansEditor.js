function modifierLangageDansEditor(uid, language) {
    for (
        let cursor = 0, cursorMax = editors.length;
        cursor < cursorMax;
        cursor++
    ) {
        const editor = editors[cursor];
        if (uid === editor.uid) {
            window.editors[cursor].language = language;
            window.editors[cursor].editor.setOption('mode', language);
        }
    }
    return false;
}

export default modifierLangageDansEditor;