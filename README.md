# 📅 ChronosMCP

**ChronosMCP** is a minimalist, multi-language server for date and time operations, built on the Model Context Protocol (MCP).  
It provides consistent, timezone-aware datetime utilities via lightweight SDKs in multiple programming languages.

---

## 🚀 Features

✅ Retrieve the current time in UTC or any timezone  
✅ Format and parse ISO datetime strings  
✅ Convert between timezones  
✅ Compute time differences  
✅ Add or subtract time deltas  
✅ Designed for easy integration with MCP-compatible clients

---

## 🧭 Available SDKs

ChronosMCP provides dedicated SDKs for each programming language.  
Choose the SDK that fits your project:

| Language | Package | Documentation |
|----------|---------|----------------|
| 🐍 **Python** | [chronos-mcp-py](./sdks/python) | [Python SDK README](./sdks/python/README.md) |
| 🟢 **Node.js** | [chronos-mcp-js](./sdks/nodejs) | [Node.js SDK README](./sdks/nodejs/README.md) |

More SDKs will be added over time.

---

## ✨ Example Use Cases

- Unified timestamp generation in microservices
- Consistent timezone conversions in distributed systems
- Formatting and parsing datetime strings in a predictable way
- Automating date calculations (e.g., scheduling workflows)

---

## 📂 Repository Structure

```
chronosMCP/
├── sdks/          # Language-specific SDKs
│   ├── python/    # Python SDK
│   └── nodejs/    # Node.js SDK
├── docs/          # Shared documentation
├── examples/      # Usage examples
└── README.md      # This file
```

---

## 🛠️ Requirements

Each SDK has its own requirements and installation instructions.  
Please refer to the respective README:

- [Python SDK](./sdks/python/README.md)
- [Node.js SDK](./sdks/nodejs/README.md)

---

## 📝 License

MIT License – see LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome!  
If you want to add a new language SDK or improve existing tools:

1. Fork this repository
2. Create a feature branch
3. Submit a pull request

Feel free to open issues with questions or ideas.

---

## 🌐 Links

- [Model Context Protocol](https://modelcontext.org)
- [ChronosMCP Documentation](./docs/index.md)

---

Happy coding! 🚀