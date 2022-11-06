import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Edge, Config

st.set_page_config(page_title="Generative AI Database",
                   page_icon=":boom:", layout="wide")
with st.container():
    st.write("""
    # Generative AI Visualization

    AI content generation category🗨️: (input => output)

    """)


def load_data1():
    return pd.DataFrame(
        {
            "category":         ["• classification",
                                 "• generation",
                                 "• transformation",
                                 ],
            "input => output":  ["image => text",
                                 "text => image",
                                 "image => image (or text => text)",
                                 ],
            "description":      ["finding, analysis, extraction from existing input",
                                 "use ML to create new output",
                                 "altering & rendering output",
                                 ],

        }
    )


df = load_data1()
st.dataframe(df)
st.image("https://pbs.twimg.com/media/FgWJonRWYAAHcMz?format=jpg&name=4096x4096")


def load_data2():
    return pd.DataFrame(
        {
            "generative ai": ["text-to-3D (T2D)",
                              "text-to-NFT (T2N)",
                              "text-to-gif (T2G)",
                              "text-to-code (T2C)",
                              "image-to-VR (I2Vr)",
                              "image-to-AR (I2Ar)",
                              "text-to-text (T2T)",
                              "text-to-image (T2I)",
                              "text-to-audio (T2S)",
                              "text-to-video (T2V)",
                              "text-to-music (T2M)",
                              "brain-to-text (B2T)",
                              "image-to-text (I2T)",
                              "speech-to-text (S2T)",
                              "audio-to-audio (A2A)",
                              "text-to-motion (T2Mo)",
                              "tweet-to-image (Tw2I)",
                              "text-to-JavaScript (T2js)", ],
            "no. of projects": [3,
                                1,
                                0,
                                2,
                                0,
                                0,
                                25,
                                13,
                                5,
                                5,
                                0,
                                2,
                                2,
                                3,
                                2,
                                2,
                                0,
                                0, ],
        }
    )


st.checkbox("Use width", value=True, key="use_container_width")
df = load_data2()
st.dataframe(df, use_container_width=st.session_state.use_container_width)

st.image("https://pbs.twimg.com/media/FgQO-4BXgAQV1PJ?format=jpg&name=4096x4096")

# The visualization
st.write("""
## The Project Visualization
""")
nodes = []
edges = []
nodes.append(Node(id="generativeAI",
                  label="Generative AI",
                  size=35,
                  shape="circularImage",
                  image="https://pbs.twimg.com/profile_images/1505494941585317890/ZtQDwyhk_400x400.png")
             )  # includes **kwargs


# 1: text-to-image (T2I)
edges.append(Edge(source="T2I",
                  label="",
                  target="generativeAI",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="T2I",
                  label="text-to-image (T2I)",
                  size=25,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
# 1: Projects List
edges.append(Edge(source="dalle",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="dalle",
                  label="DALL-E 2",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="https://pbs.twimg.com/profile_images/1512117240094547987/Viv0eNk__400x400.jpg")
             )
edges.append(Edge(source="stabledefusion",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="stabledefusion",
                  label="Stable Defusion",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Imagen",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Imagen",
                  label="Imagen",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Midjourney",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Midjourney",
                  label="Midjourney",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Wonder",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Wonder",
                  label="Wonder",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Nightcafe",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Nightcafe",
                  label="Nightcafe",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Neural.love",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Neural.love",
                  label="Neural.love",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Wombo",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Wombo",
                  label="Wombo",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Craiyon",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Craiyon",
                  label="Craiyon",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="GauGAN2ByNVIDIA",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="GauGAN2ByNVIDIA",
                  label="GauGAN2 By NVIDIA",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Pixray",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Pixray",
                  label="Pixray",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Supercreator.ai",
                  label="",
                  target="T2I",
                  color="blue",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Supercreator.ai",
                  label="Supercreator.ai",
                  size=15,
                  color="blue",
                  shape="circularImage",
                  image="")
             )


# 2: text-to-text (T2T)
edges.append(Edge(source="T2T",
                  label="",
                  target="generativeAI",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="T2T",
                  label="text-to-text (T2T)",
                  size=25,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )

# 2: Projects List
edges.append(Edge(source="gpt3",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="gpt3",
                  label="GPT-3",
                  size=15,
                  shape="circularImage",
                  image="https://pbs.twimg.com/profile_images/1512117240094547987/Viv0eNk__400x400.jpg")
             )
edges.append(Edge(source="goose.ai",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="goose.ai",
                  label="goose.ai",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="cohere.ai",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="cohere.ai",
                  label="cohere.ai",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Writesonic",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Writesonic",
                  label="Writesonic",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="jasper.ai",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="jasper.ai",
                  label="jasper.ai",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="text.cortext",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="text.cortext",
                  label="text.cortext",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="chibi.ai",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="chibi.ai",
                  label="chibi.ai",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="copy.ai",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="copy.ai",
                  label="copy.ai",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="CopySmith",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="CopySmith",
                  label="CopySmith",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Nichess",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Nichess",
                  label="Nichess",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Simplified",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Simplified",
                  label="Simplified",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Grammarly",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Grammarly",
                  label="Grammarly",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="HubSpot",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="HubSpot",
                  label="HubSpot",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="MarketMuse",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="MarketMuse",
                  label="MarketMuse",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Frase",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Frase",
                  label="Frase",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="AI12.com",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="AI12.com",
                  label="AI12.com",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="GPT-J",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="GPT-J",
                  label="GPT-J",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Inferkit",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Inferkit",
                  label="Inferkit",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Flowrite",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Flowrite",
                  label="Flowrite",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="BlogIdeaGenerator",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="BlogIdeaGenerator",
                  label="Blog Idea Generator",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Sudowrite",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Sudowrite",
                  label="Sudowrite",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="ResearchAI",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="ResearchAI",
                  label="ResearchAI",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="IdeasAI",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="IdeasAI",
                  label="IdeasAI",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="ideasbyai",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="ideasbyai",
                  label="ideasbyai",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )
edges.append(Edge(source="Requstory",
                  label="",
                  target="T2T",
                  color="Cyan",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Requstory",
                  label="Requstory",
                  size=15,
                  shape="circularImage",
                  color="Cyan",
                  image="")
             )


# 3: text-to-NFT (T2I)
edges.append(Edge(source="T2N",
                  label="",
                  target="generativeAI",
                  color="#b0fc2c",
                  # **kwargs
                  )
             )
nodes.append(Node(id="T2N",
                  label="text-to-NFT (T2N)",
                  size=25,
                  color="#b0fc2c",
                  shape="circularImage",
                  image="")
             )
# 3: Projects List
edges.append(Edge(source="LensAI",
                  label="",
                  target="T2N",
                  color="#b0fc2c",
                  # **kwargs
                  )
             )
nodes.append(Node(id="LensAI",
                  label="LensAI",
                  size=15,
                  color="#b0fc2c",
                  shape="circularImage",
                  image="https://pbs.twimg.com/profile_images/1490782523701481474/DtyJ_8ej_400x400.jpg")
             )

# 4: image-to-text (I2T)
edges.append(Edge(source="I2T",
                  label="",
                  target="generativeAI",
                  color="orange",
                  # **kwargs
                  )
             )
nodes.append(Node(id="I2T",
                  label="image-to-text (I2T)",
                  size=25,
                  color="orange",
                  shape="circularImage",
                  image="")
             )
# 4: Projects List
edges.append(Edge(source="Neural.love-2",
                  label="",
                  target="I2T",
                  color="orange",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Neural.love-2",
                  label="Neural.love ",
                  size=15,
                  color="orange",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="GPT3xImageCaptions",
                  label="",
                  target="I2T",
                  color="orange",
                  # **kwargs
                  )
             )
nodes.append(Node(id="GPT3xImageCaptions",
                  label="GPT-3 x Image Captions",
                  size=15,
                  color="orange",
                  shape="circularImage",
                  image="")
             )

# 5: text-to-code (T2C)
edges.append(Edge(source="T2C",
                  label="",
                  target="generativeAI",
                  color="Grey",
                  # **kwargs
                  )
             )
nodes.append(Node(id="T2C",
                  label="text-to-code (T2C)",
                  size=25,
                  color="Grey",
                  shape="circularImage",
                  image="")
             )
# 5: Projects List
edges.append(Edge(source="githubcopilot",
                  label="",
                  target="T2C",
                  color="Grey",
                  # **kwargs
                  )
             )
nodes.append(Node(id="githubcopilot",
                  label="GitHub Co-pilot",
                  size=15,
                  color="Grey",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="ReplitCodeGenerator",
                  label="",
                  target="T2C",
                  color="Grey",
                  # **kwargs
                  )
             )
nodes.append(Node(id="ReplitCodeGenerator",
                  label="Replit Code Generator",
                  size=15,
                  color="Grey",
                  shape="circularImage",
                  image="")
             )

# 6: text-to-video (T2V)
edges.append(Edge(source="T2V",
                  label="",
                  target="generativeAI",
                  color="Pink",
                  # **kwargs
                  )
             )
nodes.append(Node(id="T2V",
                  label="text-to-video (T2V)",
                  size=25,
                  color="Pink",
                  shape="circularImage",
                  image="")
             )
# 6: Projects List
edges.append(Edge(source="Syneshtesia",
                  label="",
                  target="T2V",
                  color="Pink",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Syneshtesia",
                  label="Syneshtesia",
                  size=15,
                  color="Pink",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="RunwayML",
                  label="",
                  target="T2V",
                  color="Pink",
                  # **kwargs
                  )
             )
nodes.append(Node(id="RunwayML",
                  label="RunwayML",
                  size=15,
                  color="Pink",
                  shape="circularImage",
                  image="https://pbs.twimg.com/profile_images/1542885861330673664/ukf6-PFA_400x400.jpg")
             )
edges.append(Edge(source="fliki",
                  label="",
                  target="T2V",
                  color="Pink",
                  # **kwargs
                  )
             )
nodes.append(Node(id="fliki",
                  label="fliki",
                  size=15,
                  color="Pink",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="MetaAI",
                  label="",
                  target="T2V",
                  color="Pink",
                  # **kwargs
                  )
             )
nodes.append(Node(id="MetaAI",
                  label="MetaAI",
                  size=15,
                  color="Pink",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Phenaki",
                  label="",
                  target="T2V",
                  color="Pink",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Phenaki",
                  label="Phenaki",
                  size=15,
                  color="Pink",
                  shape="circularImage",
                  image="")
             )


# 7: audio-to-text (A2T)
edges.append(Edge(source="A2T",
                  label="",
                  target="generativeAI",
                  color="black",
                  # **kwargs
                  )
             )
nodes.append(Node(id="A2T",
                  label="audio-to-text (A2T)",
                  size=25,
                  color="black",
                  shape="circularImage",
                  image="")
             )
# 7: Projects List
edges.append(Edge(source="Descript",
                  label="",
                  target="A2T",
                  color="black",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Descript",
                  label="Descript",
                  size=15,
                  color="black",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="AssemblyAI",
                  label="",
                  target="A2T",
                  color="black",
                  # **kwargs
                  )
             )
nodes.append(Node(id="AssemblyAI",
                  label="AssemblyAI",
                  size=15,
                  color="black",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Whisper",
                  label="",
                  target="A2T",
                  color="black",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Whisper",
                  label="Whisper (OpenAI) ",
                  size=15,
                  color="black",
                  shape="circularImage",
                  image="")
             )

# 8: text-to-audio (T2A)
edges.append(Edge(source="T2A",
                  label="",
                  target="generativeAI",
                  color="Olive",
                  # **kwargs
                  )
             )
nodes.append(Node(id="T2A",
                  label="text-to-audio (T2A)",
                  size=25,
                  color="Olive",
                  shape="circularImage",
                  image="")
             )
# 8: Projects List
edges.append(Edge(source="Descript1",
                  label="",
                  target="T2A",
                  color="Olive",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Descript1",
                  label="Descript",
                  size=15,
                  color="Olive",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="wellsaid",
                  label="",
                  target="T2A",
                  color="Olive",
                  # **kwargs
                  )
             )
nodes.append(Node(id="wellsaid",
                  label="wellsaid",
                  size=15,
                  color="Olive",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="Resemble",
                  label="",
                  target="T2A",
                  color="Olive",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Resemble",
                  label="Resemble",
                  size=15,
                  color="Olive",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="PlayHT",
                  label="",
                  target="T2A",
                  color="Olive",
                  # **kwargs
                  )
             )
nodes.append(Node(id="PlayHT",
                  label="Play HT",
                  size=15,
                  color="Olive",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="murf",
                  label="",
                  target="T2A",
                  color="Olive",
                  # **kwargs
                  )
             )
nodes.append(Node(id="murf",
                  label="murf",
                  size=15,
                  color="Olive",
                  shape="circularImage",
                  image="")
             )


# 9: audio-to-audio (A2A)
edges.append(Edge(source="A2A",
                  label="",
                  target="generativeAI",
                  color="Maroon",
                  # **kwargs
                  )
             )
nodes.append(Node(id="A2A",
                  label="audio-to-audio (A2A)",
                  size=25,
                  color="Maroon",
                  shape="circularImage",
                  image="")
             )
# 9: Projects List
edges.append(Edge(source="Voicemod",
                  label="",
                  target="A2A",
                  color="Maroon",
                  # **kwargs
                  )
             )
nodes.append(Node(id="Voicemod",
                  label="Voicemod",
                  size=15,
                  color="Maroon",
                  shape="circularImage",
                  image="")
             )
edges.append(Edge(source="AudioLM",
                  label="",
                  target="A2A",
                  color="Maroon",
                  # **kwargs
                  )
             )
nodes.append(Node(id="AudioLM",
                  label="AudioLM",
                  size=15,
                  color="Maroon",
                  shape="circularImage",
                  image="")
             )


# Others
config = Config(width=800,
                height=700,
                # **kwargs
                )

return_value = agraph(nodes=nodes,
                      edges=edges,
                      config=config)


st.write("[Follow @aaronsiim on Twitter >](https://twitter.com/aaronsiim)")
st.image("https://pbs.twimg.com/profile_images/1588722012263849984/DRJPu5eD_400x400.png",
         width=35,
         )
