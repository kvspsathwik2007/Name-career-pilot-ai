import streamlit as st


def load_css():

    st.html(
        """
        <style>

        /* =========================================================
           CAREERPILOT AI
           COMMAND CENTER V3
           Native Streamlit + CSS Motion System
        ========================================================= */


        /* =========================================================
           DESIGN TOKENS
        ========================================================= */

        :root {
            --void: #020617;
            --void-soft: #030712;

            --purple: #8b5cf6;
            --purple-light: #c4b5fd;

            --cyan: #06b6d4;
            --cyan-light: #67e8f9;

            --green: #10b981;
            --green-light: #6ee7b7;

            --amber: #f59e0b;
            --red: #ef4444;

            --white: #f8fafc;
            --text: #e2e8f0;
            --muted: #94a3b8;

            --glass:
                rgba(15, 23, 42, 0.64);

            --glass-strong:
                rgba(15, 23, 42, 0.82);

            --border:
                rgba(139, 92, 246, 0.22);

            --border-active:
                rgba(6, 182, 212, 0.72);
        }


        /* =========================================================
           GLOBAL APPLICATION
        ========================================================= */

        .stApp {

            background:

                radial-gradient(
                    circle at 8% 8%,
                    rgba(139, 92, 246, 0.17),
                    transparent 24%
                ),

                radial-gradient(
                    circle at 92% 12%,
                    rgba(6, 182, 212, 0.13),
                    transparent 24%
                ),

                radial-gradient(
                    circle at 50% 92%,
                    rgba(139, 92, 246, 0.10),
                    transparent 30%
                ),

                linear-gradient(
                    135deg,
                    #020617 0%,
                    #030712 48%,
                    #020617 100%
                );

            background-size:
                180% 180%;

            animation:
                cosmicBackground
                20s
                ease-in-out
                infinite
                alternate;

            color:
                var(--text);
        }


        @keyframes cosmicBackground {

            0% {
                background-position:
                    0% 0%;
            }

            50% {
                background-position:
                    100% 50%;
            }

            100% {
                background-position:
                    30% 100%;
            }
        }


        /* =========================================================
           STARFIELD
        ========================================================= */

        .stApp::before {

            content: "";

            position: fixed;

            inset: 0;

            pointer-events: none;

            z-index: 0;

            opacity: 0.28;

            background-image:

                radial-gradient(
                    1px 1px at 8% 12%,
                    #ffffff,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 18% 65%,
                    #67e8f9,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 32% 25%,
                    #c4b5fd,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 48% 80%,
                    #ffffff,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 65% 35%,
                    #67e8f9,
                    transparent
                ),

                radial-gradient(
                    1px 1px at 78% 72%,
                    #c4b5fd,
                    transparent
                ),

                radial-gradient(
                    2px 2px at 91% 18%,
                    #ffffff,
                    transparent
                ),

                radial-gradient(
                    2px 2px at 84% 88%,
                    #67e8f9,
                    transparent
                );

            background-size:
                320px 320px;

            animation:
                starfieldMove
                35s
                linear
                infinite;
        }


        @keyframes starfieldMove {

            from {
                transform:
                    translate3d(
                        0,
                        0,
                        0
                    );
            }

            to {
                transform:
                    translate3d(
                        -180px,
                        100px,
                        0
                    );
            }
        }


        /* =========================================================
           CONTENT LAYER
        ========================================================= */

        .main .block-container {

            position:
                relative;

            z-index:
                2;

            max-width:
                1550px;

            padding-top:
                2.2rem;

            padding-bottom:
                5rem;

            animation:
                pageEntrance
                0.8s
                cubic-bezier(
                    .2,
                    .8,
                    .2,
                    1
                );
        }


        @keyframes pageEntrance {

            from {
                opacity:
                    0;

                transform:
                    translateY(25px);
            }

            to {
                opacity:
                    1;

                transform:
                    translateY(0);
            }
        }


        /* =========================================================
           TYPOGRAPHY
        ========================================================= */

        html,
        body,
        [class*="css"] {

            font-family:
                "Inter",
                sans-serif;
        }


        h1,
        h2,
        h3,
        h4 {

            font-family:
                "Space Grotesk",
                sans-serif;

            color:
                var(--white);
        }


        h1 {

            background:

                linear-gradient(
                    90deg,
                    #ffffff,
                    #c4b5fd,
                    #67e8f9,
                    #ffffff
                );

            background-size:
                300% auto;

            -webkit-background-clip:
                text;

            -webkit-text-fill-color:
                transparent;

            animation:
                titleShimmer
                6s
                linear
                infinite;
        }


        @keyframes titleShimmer {

            from {
                background-position:
                    0% center;
            }

            to {
                background-position:
                    300% center;
            }
        }


        /* =========================================================
           SIDEBAR
        ========================================================= */

        section[data-testid="stSidebar"] {

            background:

                radial-gradient(
                    circle at 20% 10%,
                    rgba(139,92,246,.10),
                    transparent 30%
                ),

                linear-gradient(
                    180deg,
                    #020617,
                    #0b1120
                );

            border-right:
                1px solid
                rgba(139,92,246,.22);

            box-shadow:
                15px 0 60px
                rgba(0,0,0,.35);
        }


        section[data-testid="stSidebar"] * {

            font-family:
                "Inter",
                sans-serif;
        }


        /* =========================================================
           SIDEBAR NAVIGATION
        ========================================================= */

        section[data-testid="stSidebar"]
        [data-testid="stPageLink-NavLink"] {

            border-radius:
                12px;

            margin:
                3px 0;

            transition:
                all
                .25s
                ease;
        }


        section[data-testid="stSidebar"]
        [data-testid="stPageLink-NavLink"]:hover {

            background:
                rgba(139,92,246,.12);

            transform:
                translateX(5px);

            box-shadow:
                inset 3px 0 0
                var(--cyan);
        }


        /* =========================================================
           NATIVE METRIC CARDS
        ========================================================= */

        [data-testid="stMetric"] {

            position:
                relative;

            overflow:
                hidden;

            min-height:
                125px;

            padding:
                18px;

            border-radius:
                18px;

            background:
                linear-gradient(
                    145deg,
                    rgba(15,23,42,.82),
                    rgba(15,23,42,.52)
                );

            border:
                1px solid
                var(--border);

            backdrop-filter:
                blur(20px);

            box-shadow:
                0 15px 45px
                rgba(0,0,0,.25);

            transition:
                transform
                .35s
                cubic-bezier(.2,.8,.2,1),

                border-color
                .35s
                ease,

                box-shadow
                .35s
                ease;

            animation:
                metricEntrance
                .8s
                ease
                both;
        }


        [data-testid="stMetric"]::before {

            content: "";

            position:
                absolute;

            top:
                0;

            left:
                -100%;

            width:
                80%;

            height:
                1px;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    var(--cyan),
                    transparent
                );

            animation:
                metricScan
                4s
                linear
                infinite;
        }


        [data-testid="stMetric"]:hover {

            transform:
                translateY(-8px)
                scale(1.015);

            border-color:
                var(--border-active);

            box-shadow:

                0 22px 60px
                rgba(0,0,0,.38),

                0 0 30px
                rgba(6,182,212,.12);
        }


        @keyframes metricEntrance {

            from {

                opacity:
                    0;

                transform:
                    translateY(22px)
                    scale(.97);
            }

            to {

                opacity:
                    1;

                transform:
                    translateY(0)
                    scale(1);
            }
        }


        @keyframes metricScan {

            0% {
                left:
                    -100%;
            }

            100% {
                left:
                    130%;
            }
        }


        [data-testid="stMetricValue"] {

            font-family:
                "Space Grotesk",
                sans-serif;

            font-weight:
                800;

            color:
                #ffffff
                !important;
        }


        /* =========================================================
           PROGRESS BARS
        ========================================================= */

        [data-testid="stProgressBar"] {

            margin-top:
                8px;
        }


        [data-testid="stProgressBar"]
        > div {

            background:
                rgba(255,255,255,.06);

            border-radius:
                999px;
        }


        [data-testid="stProgressBar"]
        > div
        > div {

            background:

                linear-gradient(
                    90deg,
                    var(--purple),
                    var(--cyan),
                    var(--green)
                );

            background-size:
                200% 100%;

            border-radius:
                999px;

            box-shadow:
                0 0 15px
                rgba(6,182,212,.35);

            animation:
                progressEnergy
                3s
                linear
                infinite;
        }


        @keyframes progressEnergy {

            0% {
                background-position:
                    0% 50%;
            }

            100% {
                background-position:
                    200% 50%;
            }
        }


        /* =========================================================
           BUTTONS
        ========================================================= */

        .stButton > button {

            position:
                relative;

            overflow:
                hidden;

            min-height:
                44px;

            border-radius:
                12px
                !important;

            border:
                1px solid
                rgba(139,92,246,.40)
                !important;

            background:

                linear-gradient(
                    135deg,
                    rgba(139,92,246,.20),
                    rgba(6,182,212,.08)
                )
                !important;

            color:
                #ffffff
                !important;

            font-weight:
                700
                !important;

            transition:
                transform
                .25s
                ease,

                border-color
                .25s
                ease,

                box-shadow
                .25s
                ease;
        }


        .stButton > button::before {

            content: "";

            position:
                absolute;

            top:
                0;

            left:
                -120%;

            width:
                70%;

            height:
                100%;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    rgba(255,255,255,.12),
                    transparent
                );

            transform:
                skewX(-20deg);

            transition:
                left
                .5s
                ease;
        }


        .stButton > button:hover {

            transform:
                translateY(-4px)
                scale(1.02)
                !important;

            border-color:
                rgba(6,182,212,.85)
                !important;

            box-shadow:

                0 10px 30px
                rgba(0,0,0,.30),

                0 0 25px
                rgba(6,182,212,.16)
                !important;
        }


        .stButton > button:hover::before {

            left:
                140%;
        }


        .stButton > button:active {

            transform:
                scale(.96)
                !important;
        }


        /* =========================================================
           ALERTS
        ========================================================= */

        [data-testid="stAlert"] {

            border-radius:
                15px;

            backdrop-filter:
                blur(15px);

            animation:
                alertEntrance
                .5s
                ease;
        }


        @keyframes alertEntrance {

            from {

                opacity:
                    0;

                transform:
                    translateX(-18px);
            }

            to {

                opacity:
                    1;

                transform:
                    translateX(0);
            }
        }


        /* =========================================================
           EXPANDERS
        ========================================================= */

        [data-testid="stExpander"] {

            border:
                1px solid
                rgba(139,92,246,.22);

            border-radius:
                15px;

            background:
                rgba(15,23,42,.52);

            transition:
                all
                .3s
                ease;
        }


        [data-testid="stExpander"]:hover {

            border-color:
                rgba(6,182,212,.60);

            box-shadow:
                0 0 30px
                rgba(6,182,212,.08);

            transform:
                translateY(-2px);
        }


        /* =========================================================
           TEXT INPUTS
        ========================================================= */

        .stTextInput input,
        .stTextArea textarea {

            background:
                rgba(15,23,42,.75)
                !important;

            color:
                #ffffff
                !important;

            border:
                1px solid
                rgba(139,92,246,.28)
                !important;

            border-radius:
                12px
                !important;

            transition:
                border-color
                .25s
                ease,

                box-shadow
                .25s
                ease;
        }


        .stTextInput input:focus,
        .stTextArea textarea:focus {

            border-color:
                var(--cyan)
                !important;

            box-shadow:
                0 0 25px
                rgba(6,182,212,.13)
                !important;
        }


        /* =========================================================
           SELECT BOX
        ========================================================= */

        div[data-baseweb="select"] > div {

            background:
                rgba(15,23,42,.75)
                !important;

            border:
                1px solid
                rgba(139,92,246,.28)
                !important;

            border-radius:
                12px
                !important;
        }


        /* =========================================================
           FILE UPLOADER
        ========================================================= */

        [data-testid="stFileUploader"] {

            border:
                1px dashed
                rgba(6,182,212,.40);

            border-radius:
                18px;

            background:
                rgba(15,23,42,.45);

            transition:
                all
                .3s
                ease;
        }


        [data-testid="stFileUploader"]:hover {

            border-color:
                var(--cyan);

            background:
                rgba(6,182,212,.05);

            box-shadow:
                0 0 30px
                rgba(6,182,212,.08);
        }


        /* =========================================================
           TABS
        ========================================================= */

        .stTabs [data-baseweb="tab-list"] {

            gap:
                5px;

            padding:
                5px;

            border-radius:
                14px;

            background:
                rgba(15,23,42,.50);
        }


        .stTabs [data-baseweb="tab"] {

            border-radius:
                10px;

            transition:
                all
                .25s
                ease;
        }


        .stTabs [data-baseweb="tab"]:hover {

            color:
                var(--cyan);
        }


        /* =========================================================
           DIVIDERS
        ========================================================= */

        hr {

            border-color:
                rgba(139,92,246,.18)
                !important;
        }


        /* =========================================================
           SPINNER
        ========================================================= */

        [data-testid="stSpinner"] {

            animation:
                spinnerPulse
                1.2s
                ease-in-out
                infinite;
        }


        @keyframes spinnerPulse {

            0%,
            100% {
                opacity:
                    .5;
            }

            50% {
                opacity:
                    1;
            }
        }


        /* =========================================================
           SCROLLBAR
        ========================================================= */

        ::-webkit-scrollbar {

            width:
                8px;
        }


        ::-webkit-scrollbar-track {

            background:
                #020617;
        }


        ::-webkit-scrollbar-thumb {

            background:
                linear-gradient(
                    var(--purple),
                    var(--cyan)
                );

            border-radius:
                999px;
        }


        /* =========================================================
           MOBILE
        ========================================================= */

        @media (max-width: 900px) {

            .main .block-container {

                padding:
                    1rem;
            }

            h1 {

                font-size:
                    2rem;
            }

            [data-testid="stMetric"] {

                min-height:
                    105px;
            }
        }


        /* =========================================================
           REDUCED MOTION
        ========================================================= */

        @media (prefers-reduced-motion: reduce) {

            *,
            *::before,
            *::after {

                animation-duration:
                    0.01ms
                    !important;

                animation-iteration-count:
                    1
                    !important;

                transition-duration:
                    0.01ms
                    !important;
            }
        }

        </style>
        """
    )