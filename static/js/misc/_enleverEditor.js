function enleverEditor(uid) {
    for (
        let cursor = 0, cursorMax = editors.length;
        cursor < cursorMax;
        cursor++
    ) {
        const editor = editors[cursor];
        console.log({uid});
        if (uid === editor.uid) {
            let editors = window.editors;
            editors.splice(cursor, 1)
            window.editors = editors;
        }
    }
    return false;
}

export default enleverEditor;