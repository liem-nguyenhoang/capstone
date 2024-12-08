--
-- PostgreSQL database dump
--

-- Dumped from database version 16.6 (Ubuntu 16.6-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.6 (Ubuntu 16.6-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: capstone_3whg_user
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying NOT NULL,
    movie_id integer
);


ALTER TABLE public.actors OWNER TO capstone_3whg_user;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: capstone_3whg_user
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.actors_id_seq OWNER TO capstone_3whg_user;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: capstone_3whg_user
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: capstone_3whg_user
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO capstone_3whg_user;

--
-- Name: movies; Type: TABLE; Schema: public; Owner: capstone_3whg_user
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying NOT NULL,
    release_date timestamp without time zone NOT NULL
);


ALTER TABLE public.movies OWNER TO capstone_3whg_user;

--
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: capstone_3whg_user
--

CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.movies_id_seq OWNER TO capstone_3whg_user;

--
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: capstone_3whg_user
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: capstone_3whg_user
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: capstone_3whg_user
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: capstone_3whg_user
--

COPY public.actors (id, name, age, gender, movie_id) FROM stdin;
6	Actor_6	45	M	1
1	Actor_1	54	M	2
2	Actor_2	44	M	3
3	Actor_3	35	F	3
4	Actor_4	45	M	2
5	Actor_5	45	F	2
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: capstone_3whg_user
--

COPY public.alembic_version (version_num) FROM stdin;
93bb5ea98cc9
\.


--
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: capstone_3whg_user
--

COPY public.movies (id, title, release_date) FROM stdin;
2	Movie_2	2012-05-04 00:00:00
3	Movie_3	2010-05-14 00:00:00
4	Movie_4	2019-09-11 00:00:00
5	Movie_5	2020-02-19 00:00:00
1	Movie_1	2016-05-04 00:00:00
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: capstone_3whg_user
--

SELECT pg_catalog.setval('public.actors_id_seq', 6, true);


--
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: capstone_3whg_user
--

SELECT pg_catalog.setval('public.movies_id_seq', 5, true);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: capstone_3whg_user
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: capstone_3whg_user
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: capstone_3whg_user
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


--
-- Name: actors actors_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: capstone_3whg_user
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id);


--
-- PostgreSQL database dump complete
--

