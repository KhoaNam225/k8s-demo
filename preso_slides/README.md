# Introduction to Kubernetes - Presentation

Interactive presentation slides created with Manim that introduce Kubernetes fundamentals, container orchestration concepts, and the problems Kubernetes solves.

## 📖 Content Overview

This presentation provides a comprehensive introduction to Kubernetes covering:

1. **Container Challenges**: The problems with managing containerized applications at scale
2. **Kubernetes Solution**: How Kubernetes addresses these challenges
3. **Core Components**: Essential Kubernetes components and their roles
4. **Basic Features**: Key features that make Kubernetes powerful
5. **Architecture Overview**: High-level view of Kubernetes architecture

## 🎥 Viewing the Presentation

### Option 1: Direct Browser Access

Simply double-click the `final_slide.html` file to open it in your default browser.

## 🛠️ Development

The slides are generated using Manim (Mathematical Animation Engine):

### Prerequisites

- Python 3.11+
- Manim Community Edition

### Setup

```bash
# Install dependencies
uv sync

# Run the slide generation
cd main/
uv run python main.py
```

### Build Process

```bash
# Generate slides
./render_to_slides.sh
```

## 📁 Structure

```
preso_slides/
├── main/
│   ├── main.py              # Manim slide definitions
│   ├── final_slide.html     # Generated presentation
│   ├── render_to_slides.sh  # Build script
│   ├── clear_build_artifact.sh # Remove all artifacts produced throughout the build process
│   ├── manim.cfg           # Manim configuration
│   └── media/              # Generated assets
├── assets/                 # Static assets (logos, images)
└── demo/                   # Demo materials
```

## 🎨 Customisation

### Adding New Slides

1. Edit `main/main.py` to add new scene classes
2. Follow Manim scene patterns
3. Rebuild using the render script

### Updating Assets

- Replace files in the `assets/` directory
- Update references in `main.py`
- Regenerate slides

### Styling

- Modify colors, fonts, and layouts in `main.py`

## 🔧 Troubleshooting

**Slides Not Loading**:

- Ensure all files are in the correct directory structure
- Try serving through a local web server
- Check browser console for errors

**Build Issues**:

- Verify Python and Manim installation
- Check dependencies with `uv sync`
- Review Manim logs for errors

**Asset Missing**:

- Ensure all assets are in the `assets/` directory
- Check file paths in `main.py`
- Verify file permissions
