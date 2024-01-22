### User Requirements Specification Document
##### DIBRIS – Università di Genova. Scuola Politecnica, Software Engineering Course 80154


**VERSION : X.X**

**Authors**  
XXXX
YYYY

**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
| X.X |  | |  |

# Table of Contents

1. [Introduction](#p1)
	1. [Document Scope](#sp1.1)
	2. [Definitios and Acronym](#sp1.2) 
	3. [References](#sp1.3)
2. [System Description](#p2)
	1. [Context and Motivation](#sp2.1)
	2. [Project Objectives](#sp2.2)
3. [Requirement](#p3)
 	1. [Stakeholders](#sp3.1)
 	2. [Functional Requirements](#sp3.2)
 	3. [Non-Functional Requirements](#sp3.3)
  
  

<a name="p1"></a>

## 1. Introduction
This document contains what are the functional and non-functional requirements for a Virtual Reality project at FadeOut Software. As well as explained the reason for using those functional and non-functional sectors.

<a name="sp1.1"></a>

### 1.1 Document Scope
This paper introduces the Requirements Analysis for the Virtual Reality course of the Master of Science in Computer Engineering degree in Genoa, Italy.

<a name="sp1.2"></a>

### 1.2 Definitios and Acronym


| Acronym				| Definition | 
| ------------------------------------- | ----------- | 
| FadeOut Software					   | Company holder of WASDI |
| WASDI								   | Web Advanced Space Developer Interface |
| Workspace							   | Space on WASDI where a user can store and manipulate satellitar images |
| EO					   			   | Earth Observation |
| TIFF					   			   | Stands for Tag Image File Format. It is a file format used to store raster graphics and image information. |
| Band					   			   | Range of frequencies along the electromagnetic spectrum that the satellite measures |
| Bounding-Box						   | Imaginary rectangle that outlines an object in an image |
| CRS					   			   | Stands for Coordinate Reference System. Defines how georeferenced spatial data relates to real locations on the Earth’s surface |

<a name="sp1.3"></a>

### 1.3 References 
1. [WASDI Docs](https://wasdi.readthedocs.io/en/latest/index.html)
2. [WASDI Youtube Channel]()

<a name="p2"></a>

## 2. System Description
<a name="sp2.15"></a>
WASDI is an online platform that offers services to develop and deploy online applications that use satellite data. 
The project involves the development of a platform that helps Earth Observation (EO) experts process satellite imagery on the cloud. <br>
The company would like a new software that can, starting from an area of interest, generate a 3D view of that area and in case of floods, represent the evolution of them.
The project aims to ease the communication of the results of the applications so that decision makers can better understand the phenomena they are dealing with.

### 2.1 Context and Motivation

<a name="sp2.2"></a>

### 2.2 Project Obectives 

<a name="p3"></a>

## 3. Requirements

| Priorità | Significato | 
| --------------- | ----------- | 
| M | **Mandatory:**   |
| D | **Desiderable:** |
| O | **Optional:**    |
| E | **Future Enhancement:** |

<a name="sp3.1"></a>
### 3.1 Stakeholders

<a name="sp3.2"></a>
### 3.2 Functional Requirements 

| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.0 | The system should generate a 3D representation of a specific area of interest. |M|
| 2.0 | The system should generate a 3D representation of floods using the water depth layers present in a WASDI workspace. |M|
| 3.0 | The 3D environment should be explorable in a Web page. |M|
| 4.0 | The 3D environment should be explorable in an interactive way (virtual walk/flight), zoom in/out, pan, tilt... |M|
| 5.0 | The 3D environment should be generated in a non-interactive way. |M|
| 6.0 | The 3D environment should contain animations of the evolution of the floods. |M|
| 7.0 | The system should generate as output a video of the evolution of the floods. |D|

<a name="sp3.3"></a>
### 3.2 Non-Functional Requirements 
 
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.0 | The system can run in any environment, it doesn't need to be a WASDI application. |M|