# GitHub Workflows

This directory contains GitHub Actions workflows for the blizzardapi2 project.

## Workflows

### 1. `python-package.yml` - Main CI/CD Pipeline

**Triggers:** Push to main branch

**Jobs:**

- **checkout**: Runs tests on multiple Python versions (3.11, 3.12, 3.13)
- **publish**: Builds and publishes to PyPI (only on main branch)
- **release**: Creates GitHub releases (only after successful publish)

**Recent Fixes Applied:**

- ✅ **Fixed Git identity issue** in release job
- ✅ **Added proper Git configuration** for automated commits
- ✅ **Enhanced permissions** for package publishing
- ✅ **Improved error handling** and environment variables

### 2. `black.yml` - Code Formatting

**Triggers:** Push and pull requests

**Purpose:** Ensures code follows Black formatting standards

## Issues Fixed

### Git Identity Error

**Problem:** Release workflow failed with "Author identity unknown" error

```
ERROR Error: Author identity unknown
*** Please tell me who you are.
```

**Solution:** Added Git configuration in the release job:

```yaml
- name: Configure Git
  run: |
    git config --global user.name "github-actions[bot]"
    git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
```

### Additional Improvements

1. **Enhanced Checkout Configuration:**

   - Added `fetch-depth: 0` for full history access
   - Added explicit token configuration

2. **Better Permissions:**

   - Added `packages: write` permission for PyPI publishing

3. **Environment Variables:**
   - Explicitly defined `PYPI_API_TOKEN` environment variable

## Workflow Dependencies

The workflows require these secrets to be configured in the repository:

- `GITHUB_TOKEN` (automatically provided)
- `PYPI_API_TOKEN` (for PyPI publishing)

## Troubleshooting

### Common Issues

1. **Git Identity Errors:**

   - Ensure Git is configured in jobs that make commits
   - Use the github-actions[bot] identity for automated commits

2. **Permission Errors:**

   - Check that the workflow has the necessary permissions
   - Verify secrets are properly configured

3. **Version Bumping Issues:**
   - Ensure both `pyproject.toml` and `package.json` are updated
   - Check that the sed commands work correctly on the runner OS

### Debugging

To debug workflow issues:

1. Check the Actions tab in GitHub
2. Review the logs for specific error messages
3. Test locally with act (GitHub Actions local runner)
4. Verify all required secrets are set

## Future Improvements

Consider adding:

- [ ] Automated testing on pull requests
- [ ] Security scanning with CodeQL
- [ ] Dependency vulnerability scanning
- [ ] Automated changelog generation
- [ ] Release notes automation
- [ ] Performance testing
- [ ] Coverage reporting
