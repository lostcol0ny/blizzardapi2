// release-it config. JS instead of JSON so we can express a custom whatBump
// that suppresses noise releases (chore, ci, docs, style, test, refactor, build).
// Without this override, release-it falls back to a patch bump whenever there
// are any commits since the last tag — which is how v4.0.1 shipped from a
// chore-only PR.

const RELEASABLE_TYPES = new Set(["feat", "fix", "perf"]);

function whatBump(commits) {
  let bump = null;

  for (const commit of commits) {
    const isBreaking =
      (commit.notes || []).some((n) => /BREAKING/.test(n.title || "")) ||
      / !$| !:|^[a-z]+!:/.test(commit.header || "");

    if (isBreaking) {
      return { level: 0, reason: "BREAKING CHANGE" }; // major
    }

    if (commit.type === "feat" && bump !== 1) {
      bump = 1; // minor
    } else if (RELEASABLE_TYPES.has(commit.type) && bump === null) {
      bump = 2; // patch
    }
  }

  // null = no release. release-it skips the bump/tag/publish chain.
  return bump === null ? null : { level: bump };
}

module.exports = {
  git: {
    commitMessage: "chore: release v${version} [skip ci]",
    tagName: "v${version}",
  },
  github: {
    release: true,
    releaseName: "Release v${version}",
    releaseNotes: "${changelog}",
  },
  npm: {
    publish: false,
  },
  hooks: {
    "after:bump": [
      "sed -i 's/^version = \".*\"/version = \"${version}\"/' pyproject.toml",
    ],
  },
  plugins: {
    "@release-it/conventional-changelog": {
      preset: "conventionalcommits",
      whatBump,
    },
  },
};
