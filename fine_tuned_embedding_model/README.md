---
base_model: sentence-transformers/all-MiniLM-L6-v2
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:555
- loss:MultipleNegativesRankingLoss
widget:
- source_sentence: What does this text say about unclassified?
  sentences:
  - "these sources. \nErrors in third-party GAI components can also have downstream\
    \ impacts on accuracy and robustness. \nFor example, test datasets commonly used\
    \ to benchmark or validate models can contain label errors. \nInaccuracies in\
    \ these labels can impact the “stability” or robustness of these benchmarks, which\
    \ many \nGAI practitioners consider during the model selection process.  \nTrustworthy\
    \ AI Characteristics: Accountable and Transparent, Explainable and Interpretable,\
    \ Fair with \nHarmful Bias Managed, Privacy Enhanced, Safe, Secure and Resilient,\
    \ Valid and Reliable \n3. \nSuggested Actions to Manage GAI Risks \nThe following\
    \ suggested actions target risks unique to or exacerbated by GAI. \nIn addition\
    \ to the suggested actions below, AI risk management activities and actions set\
    \ forth in the AI \nRMF 1.0 and Playbook are already applicable for managing GAI\
    \ risks. Organizations are encouraged to"
  - "and hardware vulnerabilities; labor practices; data privacy and localization\
    \ \ncompliance; geopolitical alignment). \nData Privacy; Information Security;\
    \ \nValue Chain and Component \nIntegration; Harmful Bias and \nHomogenization\
    \ \nMG-3.1-003 \nRe-assess model risks after ﬁne-tuning or retrieval-augmented\
    \ generation \nimplementation and for any third-party GAI models deployed for\
    \ applications \nand/or use cases that were not evaluated in initial testing.\
    \ \nValue Chain and Component \nIntegration \nMG-3.1-004 \nTake reasonable measures\
    \ to review training data for CBRN information, and \nintellectual property, and\
    \ where appropriate, remove it. Implement reasonable \nmeasures to prevent, ﬂag,\
    \ or take other action in response to outputs that \nreproduce particular training\
    \ data (e.g., plagiarized, trademarked, patented, \nlicensed content or trade\
    \ secret material). \nIntellectual Property; CBRN \nInformation or Capabilities\
    \ \n \n43"
  - "• \nStage of the AI lifecycle: Risks can arise during design, development, deployment,\
    \ operation, \nand/or decommissioning. \n• \nScope: Risks may exist at individual\
    \ model or system levels, at the application or implementation \nlevels (i.e.,\
    \ for a speciﬁc use case), or at the ecosystem level – that is, beyond a single\
    \ system or \norganizational context. Examples of the latter include the expansion\
    \ of “algorithmic \nmonocultures,3” resulting from repeated use of the same model,\
    \ or impacts on access to \nopportunity, labor markets, and the creative economies.4\
    \ \n• \nSource of risk: Risks may emerge from factors related to the design, training,\
    \ or operation of the \nGAI model itself, stemming in some cases from GAI model\
    \ or system inputs, and in other cases, \nfrom GAI system outputs. Many GAI risks,\
    \ however, originate from human behavior, including \n \n \n3 “Algorithmic monocultures”\
    \ refers to the phenomenon in which repeated use of the same model or algorithm\
    \ in"
- source_sentence: What does this text say about unclassified?
  sentences:
  - "Security; Dangerous, Violent, or \nHateful Content \n \n34 \nMS-2.7-009 Regularly\
    \ assess and verify that security measures remain eﬀective and have not \nbeen\
    \ compromised. \nInformation Security \nAI Actor Tasks: AI Deployment, AI Impact\
    \ Assessment, Domain Experts, Operation and Monitoring, TEVV \n \nMEASURE 2.8:\
    \ Risks associated with transparency and accountability – as identiﬁed in the\
    \ MAP function – are examined and \ndocumented. \nAction ID \nSuggested Action\
    \ \nGAI Risks \nMS-2.8-001 \nCompile statistics on actual policy violations, take-down\
    \ requests, and intellectual \nproperty infringement for organizational GAI systems:\
    \ Analyze transparency \nreports across demographic groups, languages groups.\
    \ \nIntellectual Property; Harmful Bias \nand Homogenization \nMS-2.8-002 Document\
    \ the instructions given to data annotators or AI red-teamers. \nHuman-AI Conﬁguration\
    \ \nMS-2.8-003 \nUse digital content transparency solutions to enable the documentation\
    \ of each"
  - "information during GAI training and maintenance. \nHuman-AI Conﬁguration; Obscene,\
    \ \nDegrading, and/or Abusive \nContent; Value Chain and \nComponent Integration;\
    \ \nDangerous, Violent, or Hateful \nContent \nMS-2.6-002 \nAssess existence or\
    \ levels of harmful bias, intellectual property infringement, \ndata privacy violations,\
    \ obscenity, extremism, violence, or CBRN information in \nsystem training data.\
    \ \nData Privacy; Intellectual Property; \nObscene, Degrading, and/or \nAbusive\
    \ Content; Harmful Bias and \nHomogenization; Dangerous, \nViolent, or Hateful\
    \ Content; CBRN \nInformation or Capabilities \nMS-2.6-003 Re-evaluate safety\
    \ features of ﬁne-tuned models when the negative risk exceeds \norganizational\
    \ risk tolerance. \nDangerous, Violent, or Hateful \nContent \nMS-2.6-004 Review\
    \ GAI system outputs for validity and safety: Review generated code to \nassess\
    \ risks that may arise from unreliable downstream decision-making. \nValue Chain\
    \ and Component \nIntegration; Dangerous, Violent, or \nHateful Content"
  - "Information Integrity; Harmful Bias \nand Homogenization \nAI Actor Tasks: AI\
    \ Deployment, AI Impact Assessment, Domain Experts, End-Users, Operation and Monitoring,\
    \ TEVV \n \nMEASURE 2.10: Privacy risk of the AI system – as identiﬁed in the\
    \ MAP function – is examined and documented. \nAction ID \nSuggested Action \n\
    GAI Risks \nMS-2.10-001 \nConduct AI red-teaming to assess issues such as: Outputting\
    \ of training data \nsamples, and subsequent reverse engineering, model extraction,\
    \ and \nmembership inference risks; Revealing biometric, conﬁdential, copyrighted,\
    \ \nlicensed, patented, personal, proprietary, sensitive, or trade-marked information;\
    \ \nTracking or revealing location information of users or members of training\
    \ \ndatasets. \nHuman-AI Conﬁguration; \nInformation Integrity; Intellectual \n\
    Property \nMS-2.10-002 \nEngage directly with end-users and other stakeholders\
    \ to understand their \nexpectations and concerns regarding content provenance.\
    \ Use this feedback to"
- source_sentence: What does this text say about risk management?
  sentences:
  - "robust watermarking techniques and corresponding detectors to identify the source\
    \ of content or \nmetadata recording techniques and metadata management tools\
    \ and repositories to trace content \norigins and modiﬁcations. Further narrowing\
    \ of GAI task deﬁnitions to include provenance data can \nenable organizations\
    \ to maximize the utility of provenance data and risk management eﬀorts. \nA.1.7.\
    \ Enhancing Content Provenance through Structured Public Feedback \nWhile indirect\
    \ feedback methods such as automated error collection systems are useful, they\
    \ often lack \nthe context and depth that direct input from end users can provide.\
    \ Organizations can leverage feedback \napproaches described in the Pre-Deployment\
    \ Testing section to capture input from external sources such \nas through AI\
    \ red-teaming.  \nIntegrating pre- and post-deployment external feedback into\
    \ the monitoring process for GAI models and"
  - "tools for monitoring third-party GAI risks; Consider policy adjustments across\
    \ GAI \nmodeling libraries, tools and APIs, ﬁne-tuned models, and embedded tools;\
    \ \nAssess GAI vendors, open-source or proprietary GAI tools, or GAI service \n\
    providers against incident or vulnerability databases. \nData Privacy; Human-AI\
    \ \nConﬁguration; Information \nSecurity; Intellectual Property; \nValue Chain\
    \ and Component \nIntegration; Harmful Bias and \nHomogenization \nGV-6.1-010\
    \ \nUpdate GAI acceptable use policies to address proprietary and open-source\
    \ GAI \ntechnologies and data, and contractors, consultants, and other third-party\
    \ \npersonnel. \nIntellectual Property; Value Chain \nand Component Integration\
    \ \nAI Actor Tasks: Operation and Monitoring, Procurement, Third-party entities\
    \ \n \nGOVERN 6.2: Contingency processes are in place to handle failures or incidents\
    \ in third-party data or AI systems deemed to be \nhigh-risk. \nAction ID \nSuggested\
    \ Action \nGAI Risks \nGV-6.2-001"
  - "MEASURE 2.3: AI system performance or assurance criteria are measured qualitatively\
    \ or quantitatively and demonstrated for \nconditions similar to deployment setting(s).\
    \ Measures are documented. \nAction ID \nSuggested Action \nGAI Risks \nMS-2.3-001\
    \ Consider baseline model performance on suites of benchmarks when selecting a\
    \ \nmodel for ﬁne tuning or enhancement with retrieval-augmented generation. \n\
    Information Security; \nConfabulation \nMS-2.3-002 Evaluate claims of model capabilities\
    \ using empirically validated methods. \nConfabulation; Information \nSecurity\
    \ \nMS-2.3-003 Share results of pre-deployment testing with relevant GAI Actors,\
    \ such as those \nwith system release approval authority. \nHuman-AI Conﬁguration\
    \ \n \n31 \nMS-2.3-004 \nUtilize a purpose-built testing environment such as NIST\
    \ Dioptra to empirically \nevaluate GAI trustworthy characteristics. \nCBRN Information\
    \ or Capabilities; \nData Privacy; Confabulation; \nInformation Integrity; Information\
    \ \nSecurity; Dangerous, Violent, or"
- source_sentence: What does this text say about unclassified?
  sentences:
  - "techniques such as re-sampling, re-ranking, or adversarial training to mitigate\
    \ \nbiases in the generated content. \nInformation Security; Harmful Bias \nand\
    \ Homogenization \nMG-2.2-005 \nEngage in due diligence to analyze GAI output\
    \ for harmful content, potential \nmisinformation, and CBRN-related or NCII content.\
    \ \nCBRN Information or Capabilities; \nObscene, Degrading, and/or \nAbusive Content;\
    \ Harmful Bias and \nHomogenization; Dangerous, \nViolent, or Hateful Content\
    \ \n \n41 \nMG-2.2-006 \nUse feedback from internal and external AI Actors, users,\
    \ individuals, and \ncommunities, to assess impact of AI-generated content. \n\
    Human-AI Conﬁguration \nMG-2.2-007 \nUse real-time auditing tools where they can\
    \ be demonstrated to aid in the \ntracking and validation of the lineage and authenticity\
    \ of AI-generated data. \nInformation Integrity \nMG-2.2-008 \nUse structured\
    \ feedback mechanisms to solicit and capture user input about AI-\ngenerated content\
    \ to detect subtle shifts in quality or alignment with"
  - "Human-AI Conﬁguration; Value \nChain and Component Integration \nMP-5.2-002 \n\
    Plan regular engagements with AI Actors responsible for inputs to GAI systems,\
    \ \nincluding third-party data and algorithms, to review and evaluate unanticipated\
    \ \nimpacts. \nHuman-AI Conﬁguration; Value \nChain and Component Integration\
    \ \nAI Actor Tasks: AI Deployment, AI Design, AI Impact Assessment, Aﬀected Individuals\
    \ and Communities, Domain Experts, End-\nUsers, Human Factors, Operation and Monitoring\
    \  \n \nMEASURE 1.1: Approaches and metrics for measurement of AI risks enumerated\
    \ during the MAP function are selected for \nimplementation starting with the\
    \ most signiﬁcant AI risks. The risks or trustworthiness characteristics that\
    \ will not – or cannot – be \nmeasured are properly documented. \nAction ID \n\
    Suggested Action \nGAI Risks \nMS-1.1-001 Employ methods to trace the origin and\
    \ modiﬁcations of digital content. \nInformation Integrity \nMS-1.1-002"
  - "input them directly to a GAI system, with a variety of downstream negative consequences\
    \ to \ninterconnected systems. Indirect prompt injection attacks occur when adversaries\
    \ remotely (i.e., without \na direct interface) exploit LLM-integrated applications\
    \ by injecting prompts into data likely to be \nretrieved. Security researchers\
    \ have already demonstrated how indirect prompt injections can exploit \nvulnerabilities\
    \ by stealing proprietary data or running malicious code remotely on a machine.\
    \ Merely \nquerying a closed production model can elicit previously undisclosed\
    \ information about that model. \nAnother cybersecurity risk to GAI is data poisoning,\
    \ in which an adversary compromises a training \ndataset used by a model to manipulate\
    \ its outputs or operation. Malicious tampering with data or parts \nof the model\
    \ could exacerbate risks associated with GAI system outputs. \nTrustworthy AI\
    \ Characteristics: Privacy Enhanced, Safe, Secure and Resilient, Valid and Reliable\
    \ \n2.10."
- source_sentence: What does this text say about data privacy?
  sentences:
  - "Property. We also note that some risks are cross-cutting between these categories.\
    \  \n \n4 \n1. CBRN Information or Capabilities: Eased access to or synthesis\
    \ of materially nefarious \ninformation or design capabilities related to chemical,\
    \ biological, radiological, or nuclear (CBRN) \nweapons or other dangerous materials\
    \ or agents. \n2. Confabulation: The production of conﬁdently stated but erroneous\
    \ or false content (known \ncolloquially as “hallucinations” or “fabrications”)\
    \ by which users may be misled or deceived.6 \n3. Dangerous, Violent, or Hateful\
    \ Content: Eased production of and access to violent, inciting, \nradicalizing,\
    \ or threatening content as well as recommendations to carry out self-harm or\
    \ \nconduct illegal activities. Includes diﬃculty controlling public exposure\
    \ to hateful and disparaging \nor stereotyping content. \n4. Data Privacy: Impacts\
    \ due to leakage and unauthorized use, disclosure, or de-anonymization of"
  - "information during GAI training and maintenance. \nHuman-AI Conﬁguration; Obscene,\
    \ \nDegrading, and/or Abusive \nContent; Value Chain and \nComponent Integration;\
    \ \nDangerous, Violent, or Hateful \nContent \nMS-2.6-002 \nAssess existence or\
    \ levels of harmful bias, intellectual property infringement, \ndata privacy violations,\
    \ obscenity, extremism, violence, or CBRN information in \nsystem training data.\
    \ \nData Privacy; Intellectual Property; \nObscene, Degrading, and/or \nAbusive\
    \ Content; Harmful Bias and \nHomogenization; Dangerous, \nViolent, or Hateful\
    \ Content; CBRN \nInformation or Capabilities \nMS-2.6-003 Re-evaluate safety\
    \ features of ﬁne-tuned models when the negative risk exceeds \norganizational\
    \ risk tolerance. \nDangerous, Violent, or Hateful \nContent \nMS-2.6-004 Review\
    \ GAI system outputs for validity and safety: Review generated code to \nassess\
    \ risks that may arise from unreliable downstream decision-making. \nValue Chain\
    \ and Component \nIntegration; Dangerous, Violent, or \nHateful Content"
  - "Scheurer, J. et al. (2023) Technical report: Large language models can strategically\
    \ deceive their users \nwhen put under pressure. arXiv. https://arxiv.org/abs/2311.07590\
    \ \nShelby, R. et al. (2023) Sociotechnical Harms of Algorithmic Systems: Scoping\
    \ a Taxonomy for Harm \nReduction. arXiv. https://arxiv.org/pdf/2210.05791 \n\
    Shevlane, T. et al. (2023) Model evaluation for extreme risks. arXiv. https://arxiv.org/pdf/2305.15324\
    \ \nShumailov, I. et al. (2023) The curse of recursion: training on generated\
    \ data makes models forget. arXiv. \nhttps://arxiv.org/pdf/2305.17493v2 \nSmith,\
    \ A. et al. (2023) Hallucination or Confabulation? Neuroanatomy as metaphor in\
    \ Large Language \nModels. PLOS Digital Health. \nhttps://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000388\
    \ \nSoice, E. et al. (2023) Can large language models democratize access to dual-use\
    \ biotechnology? arXiv. \nhttps://arxiv.org/abs/2306.03809"
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision 8b3219a92973c328a8e22fadcfa821b5dc75636a -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'What does this text say about data privacy?',
    'information during GAI training and maintenance. \nHuman-AI Conﬁguration; Obscene, \nDegrading, and/or Abusive \nContent; Value Chain and \nComponent Integration; \nDangerous, Violent, or Hateful \nContent \nMS-2.6-002 \nAssess existence or levels of harmful bias, intellectual property infringement, \ndata privacy violations, obscenity, extremism, violence, or CBRN information in \nsystem training data. \nData Privacy; Intellectual Property; \nObscene, Degrading, and/or \nAbusive Content; Harmful Bias and \nHomogenization; Dangerous, \nViolent, or Hateful Content; CBRN \nInformation or Capabilities \nMS-2.6-003 Re-evaluate safety features of ﬁne-tuned models when the negative risk exceeds \norganizational risk tolerance. \nDangerous, Violent, or Hateful \nContent \nMS-2.6-004 Review GAI system outputs for validity and safety: Review generated code to \nassess risks that may arise from unreliable downstream decision-making. \nValue Chain and Component \nIntegration; Dangerous, Violent, or \nHateful Content',
    'Scheurer, J. et al. (2023) Technical report: Large language models can strategically deceive their users \nwhen put under pressure. arXiv. https://arxiv.org/abs/2311.07590 \nShelby, R. et al. (2023) Sociotechnical Harms of Algorithmic Systems: Scoping a Taxonomy for Harm \nReduction. arXiv. https://arxiv.org/pdf/2210.05791 \nShevlane, T. et al. (2023) Model evaluation for extreme risks. arXiv. https://arxiv.org/pdf/2305.15324 \nShumailov, I. et al. (2023) The curse of recursion: training on generated data makes models forget. arXiv. \nhttps://arxiv.org/pdf/2305.17493v2 \nSmith, A. et al. (2023) Hallucination or Confabulation? Neuroanatomy as metaphor in Large Language \nModels. PLOS Digital Health. \nhttps://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000388 \nSoice, E. et al. (2023) Can large language models democratize access to dual-use biotechnology? arXiv. \nhttps://arxiv.org/abs/2306.03809',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset


* Size: 555 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 555 samples:
  |         | sentence_0                                                                        | sentence_1                                                                            |
  |:--------|:----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                                |
  | details | <ul><li>min: 10 tokens</li><li>mean: 11.2 tokens</li><li>max: 12 tokens</li></ul> | <ul><li>min: 156 tokens</li><li>mean: 199.37 tokens</li><li>max: 256 tokens</li></ul> |
* Samples:
  | sentence_0                                                  | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  |:------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>What does this text say about trustworthiness?</code> | <code>other systems. <br>Information Integrity; Value Chain <br>and Component Integration <br>MP-2.2-002 <br>Observe and analyze how the GAI system interacts with external networks, and <br>identify any potential for negative externalities, particularly where content <br>provenance might be compromised. <br>Information Integrity <br>AI Actor Tasks: End Users <br> <br>MAP 2.3: Scientiﬁc integrity and TEVV considerations are identiﬁed and documented, including those related to experimental <br>design, data collection and selection (e.g., availability, representativeness, suitability), system trustworthiness, and construct <br>validation <br>Action ID <br>Suggested Action <br>GAI Risks <br>MP-2.3-001 <br>Assess the accuracy, quality, reliability, and authenticity of GAI output by <br>comparing it to a set of known ground truth data and by using a variety of <br>evaluation methods (e.g., human oversight and automated evaluation, proven <br>cryptographic techniques, review of content inputs). <br>Information Integrity <br> <br>25</code>                     |
  | <code>What does this text say about unclassified?</code>    | <code>training and TEVV data; Filtering of hate speech or content in GAI system <br>training data; Prevalence of GAI-generated data in GAI system training data. <br>Harmful Bias and Homogenization <br> <br> <br>15 Winogender Schemas is a sample set of paired sentences which diﬀer only by gender of the pronouns used, <br>which can be used to evaluate gender bias in natural language processing coreference resolution systems.  <br> <br>37 <br>MS-2.11-005 <br>Assess the proportion of synthetic to non-synthetic training data and verify <br>training data is not overly homogenous or GAI-produced to mitigate concerns of <br>model collapse. <br>Harmful Bias and Homogenization <br>AI Actor Tasks: AI Deployment, AI Impact Assessment, Aﬀected Individuals and Communities, Domain Experts, End-Users, <br>Operation and Monitoring, TEVV <br> <br>MEASURE 2.12: Environmental impact and sustainability of AI model training and management activities – as identiﬁed in the MAP <br>function – are assessed and documented. <br>Action ID <br>Suggested Action <br>GAI Risks</code> |
  | <code>What does this text say about unclassified?</code>    | <code>Padmakumar, V. et al. (2024) Does writing with language models reduce content diversity? ICLR. <br>https://arxiv.org/pdf/2309.05196 <br>Park, P. et. al. (2024) AI deception: A survey of examples, risks, and potential solutions. Patterns, 5(5). <br>arXiv. https://arxiv.org/pdf/2308.14752 <br>Partnership on AI (2023) Building a Glossary for Synthetic Media Transparency Methods, Part 1: Indirect <br>Disclosure. https://partnershiponai.org/glossary-for-synthetic-media-transparency-methods-part-1-<br>indirect-disclosure/ <br>Qu, Y. et al. (2023) Unsafe Diﬀusion: On the Generation of Unsafe Images and Hateful Memes From Text-<br>To-Image Models. arXiv. https://arxiv.org/pdf/2305.13873 <br>Rafat, K. et al. (2023) Mitigating carbon footprint for knowledge distillation based deep learning model <br>compression. PLOS One. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0285668 <br>Said, I. et al. (2022) Nonconsensual Distribution of Intimate Images: Exploring the Role of Legal Attitudes</code>                                              |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: False
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `eval_use_gather_object`: False
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Framework Versions
- Python: 3.11.5
- Sentence Transformers: 3.1.1
- Transformers: 4.44.2
- PyTorch: 2.4.1+cpu
- Accelerate: 0.34.2
- Datasets: 3.0.0
- Tokenizers: 0.19.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->