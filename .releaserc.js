const types = ["feat", "fix", "chore", "docs", "style", "refactor", "perf", "test", "build", "ci"]

const types_glob = `{${types.join(",")}}`

module.exports = {
    branches: ["main"],
    plugins: [
        [
            "@semantic-release/commit-analyzer",
            {
                preset: "angular",
                releaseRules: [
                    {
                        type: types_glob,
                        subject: "*\\[MAJOR\\]*",
                        release: "major",
                    },
                    {
                        type: types_glob,
                        subject: "*\\[MINOR\\]*",
                        release: "minor",
                    },
                    {
                        type: types_glob,
                        release: "patch",
                    },
                ],
            },
        ],
        "@semantic-release/release-notes-generator",
        "@semantic-release/github",
    ],
}
