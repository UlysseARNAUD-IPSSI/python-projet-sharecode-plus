function contientEditor(uid) {
    for (
        let cursor = 0, cursorMax = editors.length;
        cursor < cursorMax;
        cursor++
    ) {
        const editor = editors[cursor];
        if (uid === editor.uid) {
            return true;
        }
    }
    return false;
}

export default contientEditor;