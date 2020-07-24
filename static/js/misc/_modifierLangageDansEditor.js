function modifierLangageDansEditor(uid, language) {
    let languages = document.querySelector('input[name="mimes"]');
    languages.value = languages.value.replace(/'/g, '"');
    languages = JSON.parse(languages.value);

    for (
        let cursor = 0, cursorMax = editors.length;
        cursor < cursorMax;
        cursor++
    ) {
        const editor = editors[cursor];
        if (uid === editor.uid) {
            window.editors[cursor].language = language;
            window.editors[cursor].editor.setOption('mode', languages[language]);
        }
    }
    return false;
}

export default modifierLangageDansEditor;