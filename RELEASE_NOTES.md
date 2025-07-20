# Metis Agent Release Notes

## v0.1.5 - January 20, 2025

### Major Features

**Phase 4: Enhanced Project Generation**
- **Multi-File Project Scaffolding**: Generate complete projects with 13-14 files
- **Framework Support**: Python APIs, React apps, Full-stack applications
- **Auto-Documentation**: Automatically generates `tasks.md`, `requirements.md`
- **Directory Structure**: Proper project organization with best practices

**New CLI Commands:**
```bash
metis generate project "FastAPI backend with PostgreSQL" --name my-api
metis generate feature "User authentication system"
metis generate api "inventory-management"
metis generate component "ProductCard"
metis generate crud "User"
```

### Bug Fixes
- Fixed `EnhancedProjectGeneratorTool` execution signature errors
- Resolved tool instantiation issues in CLI commands
- Fixed test scripts and improved error handling
- Enhanced tool registry and discovery

### Documentation
- **Complete CLI Documentation**: Comprehensive guide covering all 13 command groups
- **Best Practices**: Development workflows and examples
- **Multi-Terminal Support**: Parallel development patterns
- **Production-Ready Examples**: Real-world usage scenarios

### Performance & Quality
- All Phase 4 tests passing (3/3 scenarios)
- Production-ready multi-file generation
- Improved error messages and user experience
- Enhanced tool registration and discovery

### Installation
```bash
pip install metis-agent>=0.1.5
```

### Resources
- [Complete CLI Documentation](CLI_Documentation.md)
- [PyPI Package](https://pypi.org/project/metis-agent/0.1.5/)
- [GitHub Repository](https://github.com/metisos/metisos_agentV1)

---

**Previous Versions:**
- v0.1.4: Tool enhancements and bug fixes
- v0.1.3: Core framework and basic CLI commands
- v0.1.2: Memory system improvements  
- v0.1.1: Initial public release
