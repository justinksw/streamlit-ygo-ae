import pandas as pd
import streamlit as st

from search_filter import FILTER


df = pd.read_csv("AETable.csv", index_col=0)

df["Abilities/Other"] = df["Abilities/Other"].fillna("NaN")


# === Card Type == #


with st.expander("Card Type"):

    col1, col2, col3, col4 = st.columns(4)

    opt_card_type = [False] * len(FILTER["Card Type"])

    for i, s in enumerate(FILTER["Card Type"]):
        if i == 0 or i % 4 == 0:
            with col1:
                opt_card_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 1) % 4 == 0:
            with col2:
                opt_card_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 2) % 4 == 0:
            with col3:
                opt_card_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 3) % 4 == 0:
            with col4:
                opt_card_type[i] = st.checkbox(s, key=s, value=False)


# === Attribute === #


with st.expander("Attributes"):

    col1, col2, col3, col4 = st.columns(4)

    opt_attribute = [False] * len(FILTER["Attribute"])

    for i, s in enumerate(FILTER["Attribute"]):
        if i == 0 or i % 4 == 0:
            with col1:
                opt_attribute[i] = st.checkbox(s, key=s, value=False)
        elif (i - 1) % 4 == 0:
            with col2:
                opt_attribute[i] = st.checkbox(s, key=s, value=False)
        elif (i - 2) % 4 == 0:
            with col3:
                opt_attribute[i] = st.checkbox(s, key=s, value=False)
        elif (i - 3) % 4 == 0:
            with col4:
                opt_attribute[i] = st.checkbox(s, key=s, value=False)


# === Type of Spell and Trap === #


with st.expander("Type of Spell and Trap"):

    col1, col2, col3, col4 = st.columns(4)

    opt_spell_trap_type = [False] * len(FILTER["Type of Spell and Trap"])

    for i, s in enumerate(FILTER["Type of Spell and Trap"]):
        if i == 0 or i % 4 == 0:
            with col1:
                opt_spell_trap_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 1) % 4 == 0:
            with col2:
                opt_spell_trap_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 2) % 4 == 0:
            with col3:
                opt_spell_trap_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 3) % 4 == 0:
            with col4:
                opt_spell_trap_type[i] = st.checkbox(s, key=s, value=False)


# === Type (Monster) === #


with st.expander("Type of Monster"):

    col1, col2, col3, col4 = st.columns(4)

    opt_monster_type = [False] * len(FILTER["Type"])

    for i, s in enumerate(FILTER["Type"]):
        if i == 0 or i % 4 == 0:
            with col1:
                opt_monster_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 1) % 4 == 0:
            with col2:
                opt_monster_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 2) % 4 == 0:
            with col3:
                opt_monster_type[i] = st.checkbox(s, key=s, value=False)
        elif (i - 3) % 4 == 0:
            with col4:
                opt_monster_type[i] = st.checkbox(s, key=s, value=False)


# === Level/Rank/Link (Monster) === #


with st.expander("Level / Rank / Link"):

    col1, col2, col3, col4, col5 = st.columns(5)

    opt_monster_level = [False] * len(FILTER["Level/Rank/Link"])

    for i, s in enumerate(FILTER["Level/Rank/Link"]):
        if i == 0 or i % 5 == 0:
            with col1:
                opt_monster_level[i] = st.checkbox(s, key="lv" + s, value=False)
        elif (i - 1) % 5 == 0:
            with col2:
                opt_monster_level[i] = st.checkbox(s, key="lv" + s, value=False)
        elif (i - 2) % 5 == 0:
            with col3:
                opt_monster_level[i] = st.checkbox(s, key="lv" + s, value=False)
        elif (i - 3) % 5 == 0:
            with col4:
                opt_monster_level[i] = st.checkbox(s, key="lv" + s, value=False)
        elif (i - 4) % 5 == 0:
            with col5:
                opt_monster_level[i] = st.checkbox(s, key="lv" + s, value=False)


# === Abilities/Other (Monsters)=== #


with st.expander("Abilities/Other"):

    col1, col2, col3, col4 = st.columns(4)

    opt_monster_others = [False] * len(FILTER["Abilities/Other"])

    for i, s in enumerate(FILTER["Abilities/Other"]):
        if i == 0 or i % 4 == 0:
            with col1:
                opt_monster_others[i] = st.checkbox(s, key=s, value=False)
        elif (i - 1) % 4 == 0:
            with col2:
                opt_monster_others[i] = st.checkbox(s, key=s, value=False)
        elif (i - 2) % 4 == 0:
            with col3:
                opt_monster_others[i] = st.checkbox(s, key=s, value=False)
        elif (i - 3) % 4 == 0:
            with col4:
                opt_monster_others[i] = st.checkbox(s, key=s, value=False)


# === st.session_state variables === #


if "select_attribute" not in st.session_state:
    st.session_state["select_attribute"] = False
    st.session_state["select_spell_trap"] = False
    st.session_state["select_monster_type"] = False
    st.session_state["select_monster_level"] = False
    st.session_state["select_monster_others"] = False


# === FILTER SETTING === #


# === Abilities/Other (Monsters)=== #


if any(opt_monster_others):
    st.session_state["select_monster_others"] = True
    filter_monster_others = [
        e for i, e in enumerate(FILTER["Abilities/Other"]) if opt_monster_others[i]
    ]

else:
    st.session_state["select_monster_others"] = False

    filter_monster_others = FILTER["Abilities/Other"].copy()
    filter_monster_others.append("NaN")


# === Level/Rank/Link (Monsters)=== #


if any(opt_monster_level):
    st.session_state["select_monster_level"] = True
    filter_monster_level = [
        int(e) for i, e in enumerate(FILTER["Level/Rank/Link"]) if opt_monster_level[i]
    ]
else:
    st.session_state["select_monster_level"] = False
    filter_monster_level = [int(e) for e in FILTER["Level/Rank/Link"]]


# === Type (Monsters)=== #


if any(opt_monster_type):
    st.session_state["select_monster_type"] = True
    filter_monster_type = [
        e for i, e in enumerate(FILTER["Type"]) if opt_monster_type[i]
    ]
else:
    st.session_state["select_monster_type"] = False
    filter_monster_type = FILTER["Type"]


# === Attribute (Monsters)=== #


if any(opt_attribute):
    st.session_state["select_attribute"] = True
    filter_attribute = [
        e for i, e in enumerate(FILTER["Attribute"]) if opt_attribute[i]
    ]
else:
    st.session_state["select_attribute"] = False
    filter_attribute = FILTER["Attribute"]


# === Type (Monsters + Spell + Trap)=== #


if any(opt_card_type):
    filter_card_types = [
        e for i, e in enumerate(FILTER["Card Type"]) if opt_card_type[i]
    ]
else:
    filter_card_types = FILTER["Card Type"]


# === Type (Spell + Trap)=== #


if any(opt_spell_trap_type):
    st.session_state["select_spell_trap"] = True

    filter_spell_trap_type = [
        e
        for i, e in enumerate(FILTER["Type of Spell and Trap"])
        if opt_spell_trap_type[i]
    ]
else:
    st.session_state["select_spell_trap"] = False


# === Filter the Dataframe === #


# === Monster === #


if (
    st.session_state["select_attribute"]
    or st.session_state["select_monster_type"]
    or st.session_state["select_monster_level"]
    or st.session_state["select_monster_others"]
):

    df = df[
        (df["Card Type"].isin(filter_card_types))
        & (df["Attribute"].isin(filter_attribute))
        & (df["Type"].isin(filter_monster_type))
        & (df["Level/Rank/Link"].isin(filter_monster_level))
        & (df["Abilities/Other"].isin(filter_monster_others))
    ]


# === Spell / Trap === #


else:
    if st.session_state["select_spell_trap"]:
        df = df[
            df["Card Type"].isin(["Spell", "Trap"])
            & df["Type of Spell and Trap"].isin(filter_spell_trap_type)
        ]

    else:
        df = df[df["Card Type"].isin(filter_card_types)]


# === Visualize === #

st.write(f"{len(df)} results")

st.dataframe(df)
