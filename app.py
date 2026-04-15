import streamlit as st
import streamlit.components.v1 as components
import moleview
import json
import uuid


def parse_xyz_data(xyz_text):
    """Parse XYZ text into atom symbols and Cartesian coordinates."""
    lines = xyz_text.splitlines()
    if len(lines) < 1:
        raise ValueError("XYZ data is too short.")

    try:
        num_atoms = int(lines[0].strip())
    except ValueError as exc:
        raise ValueError("First line of XYZ must be the number of atoms.") from exc

    atoms = []
    coords = []
    atom_lines = lines[2:] if len(lines) >= 2 else []
    for line in atom_lines:
        if len(atoms) == num_atoms:
            break
        if not line.strip():
            continue

        parts = line.split()
        if len(parts) < 4:
            raise ValueError(f"Invalid atom line: '{line}'")
        atoms.append(parts[0])
        coords.append([float(parts[1]), float(parts[2]), float(parts[3])])

    if len(atoms) != num_atoms:
        raise ValueError("XYZ data does not contain the expected number of atom lines.")

    return atoms, coords


def render_plotly_with_client_loading(fig, height=600):
    """Render Plotly with a browser-side loading overlay until draw is complete."""
    plot_spec = fig.to_plotly_json()
    plot_data_json = json.dumps(plot_spec.get("data", []))
    plot_layout_json = json.dumps(plot_spec.get("layout", {}))
    plot_config_json = json.dumps({"responsive": True})
    plot_id = f"plot-{uuid.uuid4().hex}"

    html = f"""
    <div style="position:relative; width:100%; min-height:{height}px; border:1px solid #e5e7eb; border-radius:10px; overflow:hidden;">
        <div id="loading-{plot_id}" style="position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:10px; background:#ffffff; z-index:10;">
            <div style="font-family: sans-serif; font-size:14px; color:#374151;">Rendering 3D plot...</div>
            <div style="width:60%; max-width:420px; height:10px; background:#e5e7eb; border-radius:9999px; overflow:hidden;">
                <div style="width:35%; height:100%; background:#10b981; border-radius:9999px; animation:mv-progress 1.2s ease-in-out infinite;"></div>
            </div>
        </div>
        <div id="{plot_id}" style="width:100%; height:{height}px;"></div>
    </div>

    <style>
        @keyframes mv-progress {{
            0% {{ transform: translateX(-120%); }}
            100% {{ transform: translateX(320%); }}
        }}
    </style>

    <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
    <script>
        const data = {plot_data_json};
        const layout = {plot_layout_json};
        const config = {plot_config_json};
        const plotDiv = document.getElementById("{plot_id}");
        const loading = document.getElementById("loading-{plot_id}");

        Plotly.newPlot(plotDiv, data, layout, config)
            .then(() => {{
                loading.style.display = "none";
            }})
            .catch((err) => {{
                loading.innerHTML = '<div style="font-family:sans-serif; color:#b91c1c;">Failed to render plot: ' + String(err) + '</div>';
            }});
    </script>
    """

    components.html(html, height=height + 20)


# Page configuration
st.set_page_config(page_title="MoleView Web", layout="wide")

st.title("🧪 MoleView: 3D Molecular Visualization")
# st.sidebar.header("Settings")
with st.sidebar:
    st.title("About This App")
    # st.image("path/to/your/image.png", width=100) # Optional: Add a logo
    st.write("A Fast and lightweight plug-in for 3D molecular visualization")
    st.write("Created by Rangsiman Ketkaew")
    st.markdown("---")  # Optional: Add a separator
    st.write("Version 1.2")

# 1. User Input Section
input_method = st.radio(
    "Choose input method:", ("Upload .xyz file", "Paste XYZ coordinates")
)

xyz_data = None

if input_method == "Upload .xyz file":
    uploaded_file = st.file_uploader("Upload your molecule", type=["xyz"])
    if uploaded_file is not None:
        xyz_data = uploaded_file.getvalue().decode("utf-8")

else:
    xyz_data = st.text_area(
        "Paste your XYZ coordinates here:",
        height=300,
        placeholder="3\nWater molecule\nO  0.000000 0.000000 0.000000\nH  0.757200 0.000000 0.585900\nH  -0.757200 0.000000 0.585900",
    )

visualizer = st.selectbox("Choose visualizer:", ("Plotly", "Matplotlib"))
display_clicked = st.button("Display")

# 2. Visualization Logic
if display_clicked:
    if not xyz_data:
        st.warning("Please upload an XYZ file or paste XYZ coordinates first.")
    else:
        try:
            st.subheader("3D Visualization")

            if visualizer == "Plotly":
                atoms, coords = parse_xyz_data(xyz_data)
                fig = moleview.visualize_plotly(atoms, coords, show_plot=False)
                render_plotly_with_client_loading(fig, height=600)
            else:
                atoms, coords = parse_xyz_data(xyz_data)
                fig = moleview.visualize_matplotlib(atoms, coords, show_plot=False)
                st.pyplot(fig)

            st.success("Molecule loaded successfully!")

        except Exception as e:
            st.error(f"Error processing molecule: {e}")
