// managed by bakefile; edit only the parts marked "editable"
export default {
    semi: false,
    tabWidth: 4,
    trailingComma: "es5",
    printWidth: 105,
    ignorePatterns: [
        // (editable)
        // managed-content template sources: bake renders them, so oxfmt must not reformat them
        "**/managed/",
    ],
}
