<h1 align="center">
  Consent Building Block (Govstack)
</h1>

<p align="center">
  <a href="../commits/" title="Last Commit"><img src="https://img.shields.io/github/last-commit/GovStackWorkingGroup/bb-consent?style=flat"></a>
  <a href="../issues" title="Open Issues"><img src="https://img.shields.io/github/issues/GovStackWorkingGroup/bb-consent?style=flat"></a>
  <a href="./LICENSE" title="License"><img src="https://img.shields.io/badge/License-Apache%202.0-green.svg?style=flat"></a>
</p>

<!--TODO: Update the TOC-->
<p align="center">
  <a href="#about">About</a> •
  <a href="#release-status">Release Status</a> •
  <a href="#core-team">Core Team</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#licensing">Licensing</a>
</p>

## About

Consent BB defines the principles, functions and architecture of an information system that enables services for individuals to approve the use of her/his personal data and for information system operators that process personal data of individuals to know the will of the individual and legitimately process such personal data.

It is a process-oriented GovStack BB facilitating auditable bilateral agreement within a multi-agent environment, that integrates with most other BBs.

This repository contains the deliverables from Consent BB team, as part of the Govstack project.

## Core Team

* Ain Aaviksoo ([ain.aaviksoo@guardtime.com](ain.aaviksoo@guardtime.com))
* Benjamin Balder Bach ([balder@overtag.dk](balder@overtag.dk)) 
* Philippe Page ([philippe.page@humancolossus.org](philippe.page@humancolossus.org))
* Lal Chandran ([lal@igrant.io](lal@igrant.io))

Working Group Representative: Ramkumar ([psramkumar2@gmail.com](psramkumar2@gmail.com))

## Deliverables

The key deliverables are as summarised below:

1. [Consent BB definition 0.9.0RC2](https://docs.google.com/document/d/1LR2PRhhE2YMUqnIpIKAu4IprYXXPmsMG/edit?usp=drive_web&ouid=100253799258087784406&rtpof=true)
1. Use case specifications (see Consent BB Definition)
1. Functional and technical requirements (see Consent BB Definition)
1. OpenAPI specs - Latest version: [0.9.0rc1](https://app.swaggerhub.com/apis/GovStack/consent-management-bb/)
1. Rendered diagrams and diagram sources (maintained in Git)

## Release Status

All diagrams and API specifications contained here are subject to ongoing changes by an internal GovStack Working Group, following this roadmap:

* Wave 2, Internal Review (July 14th, 2022)
* Release certification (Deadline TBA)
* Limited publication (Deadline TBA)
* Community-wide publication (~August 2022)

## Contributing

Feel free to improve the plugin and send us a pull request. If you found any problems, please create an issue in this repo.

## Licensing

Licensing is under [GNU General Public License 3.0](https://github.com/lalc/BuildingBlockAPI/blob/main/LICENSE) 

## Consent specs in Gitbook

Govstack specs are published at [Gitbook - Govstack Global](https://docs.govstack.global/).

Note that pushes to the `main` branch will automatically trigger a Gitbook build
and deployment from the `/spec` directory.

## Repo Structure

```sh
README.md
/spec # the markdown files which are used to build the specification in GitBook
/api # the openapi specification
/test # the test plan and tests
  plan.md
/examples # examples for deploying, configuring, and testing applications which implement the behaviors specified by this building block
  /application-a
    README.md # instructions for deployment/testing
    docker-compose.yaml # example deployment file
      db
      web
      adaptor
      security-server
    Caddyfile # example config for "adaptor"
    Dockerfile # dockerfile to build "adaptor"
  /application-b
  /application-c
```
