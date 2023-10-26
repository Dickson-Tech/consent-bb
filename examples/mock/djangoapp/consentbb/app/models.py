
# !!! This code is auto-generated, please do not modify

from django.db import models


class Individual(models.Model):
    """Shallowly models an Individual which may reference some instance in an external system (registration system, functional ID, foundational ID etc). An Individual instance of this model is not to be mistaken with a unique natural individual. It is up to the system owner to decide if this record permits mapping to a natural individual and/or if a single Individual row can map to several consent agreements."""
    
    externalId = models.CharField(
        verbose_name="externalId",
        help_text="Reference to another foundational/functional ID, which is likely PII",
        max_length=1024,
        null=True,
        blank=True,
    )

    externalIdType = models.CharField(
        verbose_name="externalIdType",
        help_text="External id type specifier. A string. For instance \"email\" or \"foundational id\". Can be used in later queries.",
        max_length=1024,
        null=True,
        blank=True,
    )

    identityProviderId = models.CharField(
        verbose_name="identityProviderId",
        help_text="This could be an FK, but for now we do not have a mapping of identity providers. IDBB may have more requirements.",
        max_length=1024,
        null=True,
        blank=True,
    )



class Agreement(models.Model):
    """An agreement contains the specification of a single purpose that can be consented to. An Agreement is universal and can be consented to by *many* individuals through a ConsentRecord"""
    
    version = models.CharField(
        verbose_name="version",
        help_text="The version of this specification to which a receipt conforms",
        max_length=1024,
        null=False,
        blank=False,
    )

    controller = models.ForeignKey(
        "Controller",
        verbose_name="controller",
        help_text="Data controller (may be omitted if no data involved)",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    policy = models.ForeignKey(
        "Policy",
        verbose_name="policy",
        help_text="Reference to the policy under which this Agreement shall be governed",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    purpose = models.CharField(
        verbose_name="purpose",
        help_text="Purpose of data processing or purpose of consent. Displayed to the user.",
        max_length=1024,
        null=False,
        blank=False,
    )

    lawfulBasis = models.CharField(
        verbose_name="lawfulBasis",
        help_text="Lawful basis of the agreement - consent / legal_obligation / contract / vital_interest / public_task / legitimate_interest",
        max_length=1024,
        null=False,
        blank=False,
    )

    dataUse = models.CharField(
        verbose_name="dataUse",
        help_text="null/data_source/data_using_service",
        max_length=1024,
        null=True,
        blank=True,
    )

    dpia = models.CharField(
        verbose_name="dpia",
        help_text="Data Protection Impact Assessment",
        max_length=1024,
        null=False,
        blank=False,
    )

    signature = models.ForeignKey(
        "Signature",
        verbose_name="signature",
        help_text="Signature of authorizing party of Agreement. Note: Signatures may be chained in case of multiple signatures.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    active = models.BooleanField(
        verbose_name="active",
        help_text="Agreement is active and new ConsentRecords can be created.",
        null=True,
        blank=True,
    )

    forgettable = models.BooleanField(
        verbose_name="forgettable",
        help_text="Consent Record may be deleted when consent is withdrawn, as its existence is not necessary for auditability.",
        null=True,
        blank=True,
    )

    compatibleWithVersion = models.ForeignKey(
        "Agreement",
        verbose_name="compatibleWithVersion",
        help_text="WIP: This field indicates that Consent Records may be transferred from this compatible previous version of the same Agreement.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    lifecycle = models.ForeignKey(
        "AgreementLifecycle",
        verbose_name="lifecycle",
        help_text="WIP: Current Lifecycle state of the Agreement. Lifecycle states are used to manage internal workflows and should not be assigned semantic meanings for active Consent Records.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )



class AgreementData(models.Model):
    """Agreement data contains specifications of exactly what is collected."""
    
    agreement = models.ForeignKey(
        "Agreement",
        verbose_name="agreement",
        help_text="",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Name of the attribute, for instance \"name\" or \"age\"",
        max_length=1024,
        null=False,
        blank=False,
    )

    sensitivity = models.CharField(
        verbose_name="sensitivity",
        help_text="categories of sensitivity",
        max_length=1024,
        null=False,
        blank=False,
    )

    category = models.CharField(
        verbose_name="category",
        help_text="",
        max_length=1024,
        null=False,
        blank=False,
    )



class Policy(models.Model):
    """A policy governs data and Agreement in the realm of an organisation that is refered to as \"data controller\" (GDPR) and owner of referencing Agreements."""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of the policy",
        max_length=1024,
        null=False,
        blank=False,
    )

    version = models.CharField(
        verbose_name="version",
        help_text="Version of the policy",
        max_length=1024,
        null=False,
        blank=False,
    )

    url = models.CharField(
        verbose_name="url",
        help_text="Permanent URL at which this very version of the Policy can be read, should not be allowed to change over time.",
        max_length=1024,
        null=False,
        blank=False,
    )

    jurisdiction = models.CharField(
        verbose_name="jurisdiction",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )

    industrySector = models.CharField(
        verbose_name="industrySector",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )

    dataRetentionPeriodDays = models.IntegerField(
        verbose_name="dataRetentionPeriodDays",
        help_text="",
        null=True,
        blank=True,
    )

    geographicRestriction = models.CharField(
        verbose_name="geographicRestriction",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )

    storageLocation = models.CharField(
        verbose_name="storageLocation",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )



class ConsentRecord(models.Model):
    """A Consent Record expresses consent (as defined in this building block's specification) to a single Agreement. There must be a UNIQUE constraint on (agreementRevision, individual)"""
    
    agreement = models.ForeignKey(
        "Agreement",
        verbose_name="agreement",
        help_text="The Agreement to which consent has been given",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    agreementRevision = models.ForeignKey(
        "Revision",
        verbose_name="agreementRevision",
        help_text="The Revision of the agreement which consent has been given to",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    agreementRevisionHash = models.CharField(
        verbose_name="agreementRevisionHash",
        help_text="Copy of the revision hash. The hash is the included in the signature and ensures against tampering with the original agreement.",
        max_length=1024,
        null=False,
        blank=False,
    )

    individual = models.ForeignKey(
        "Individual",
        verbose_name="individual",
        help_text="The Individual who has signed this consent record",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    optIn = models.BooleanField(
        verbose_name="optIn",
        help_text="True: The individual has positively opted in. False: The individual has explicitly said no (or withdrawn a previous consent).",
        null=True,
        blank=True,
    )

    state = models.CharField(
        verbose_name="state",
        help_text="The state field is used to record state changes after-the-fact. It is maintained by the Consent BB itself. Valid states: unsigned/pending more signatures/signed",
        max_length=1024,
        null=False,
        blank=False,
    )

    signature = models.ForeignKey(
        "Signature",
        verbose_name="signature",
        help_text="A signature that hashes all the values of the consent record and has signed it with the key of the Invidiual, making it verifiable and tamper-proof. TBD: Relation to a Signature schema?",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )



class Revision(models.Model):
    """A *generic* revision model captures the serialized contents of any shema's single row. This is then subject to 1) cryptographic signature and 2) auditing.\n\nAside from \"successor\" column, a revision should be considered locked."""
    
    schemaName = models.CharField(
        verbose_name="schemaName",
        help_text="This was previously called \"schema\" but for technical reasons should be called \"schemaName\"",
        max_length=1024,
        null=False,
        blank=False,
    )

    objectId = models.CharField(
        verbose_name="objectId",
        help_text="The PK of the object that was serialized.",
        max_length=1024,
        null=False,
        blank=False,
    )

    signedWithoutObjectId = models.BooleanField(
        verbose_name="signedWithoutObjectId",
        help_text="Indicates that objectId was left blank in serializedSnapshot when calculating serializedHash. objectId may be subsequently filled in.",
        null=True,
        blank=True,
    )

    serializedSnapshot = models.CharField(
        verbose_name="serializedSnapshot",
        help_text="Revisioned data (serialized as JSON) as a dict {objectData: {...}, schemaName: ..., objectId: ..., signedWithoutObjectId: ..., timestamp: ..., authorizedByIndividual: ..., authorizedByOther: ...}. It contains all the fields of the schema except id, successor, predessorHash and predecessorSignature.",
        max_length=1024,
        null=False,
        blank=False,
    )

    serializedHash = models.CharField(
        verbose_name="serializedHash",
        help_text="Hash of serializedSnapshot (SHA-1)",
        max_length=1024,
        null=False,
        blank=False,
    )

    timestamp = models.CharField(
        verbose_name="timestamp",
        help_text="Timestamp of when revisioning happened",
        max_length=1024,
        null=False,
        blank=False,
    )

    authorizedByIndividual = models.ForeignKey(
        "Individual",
        verbose_name="authorizedByIndividual",
        help_text="",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    authorizedByOther = models.CharField(
        verbose_name="authorizedByOther",
        help_text="Reference to an admin user that has created this revision",
        max_length=1024,
        null=True,
        blank=True,
    )

    successor = models.ForeignKey(
        "Revision",
        verbose_name="successor",
        help_text="This revision is no longer the latest revision, refer to its successor.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    predecessorHash = models.CharField(
        verbose_name="predecessorHash",
        help_text="Tamper-resistent artifact from previous record, copied from serializedHash",
        max_length=1024,
        null=True,
        blank=True,
    )

    predecessorSignature = models.CharField(
        verbose_name="predecessorSignature",
        help_text="Tamper-resistent artifact from previous record (we don't know if the previous record was signed or not)",
        max_length=1024,
        null=True,
        blank=True,
    )



class Controller(models.Model):
    """Details of a data controller."""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of data controller (may be omitted if no data involved)",
        max_length=1024,
        null=False,
        blank=False,
    )

    url = models.CharField(
        verbose_name="url",
        help_text="URL of data controller (may be omitted if no data involved)",
        max_length=1024,
        null=False,
        blank=False,
    )



class Signature(models.Model):
    """A generic signature contains a cryptographic hash of some value, together with a signature created by some private key in another system. Required signing methods: Revision object or another Signature object."""
    
    payload = models.CharField(
        verbose_name="payload",
        help_text="The final payload that is signed, constructed as a JSON serialization of fields {verificiationPayload: ..., verificationPayloadHash: ..., verificationMethod: ..., verificationArtifact: ..., verificationSignedBy: ..., verificationJwsHeader, timestamp: ..., signedWithoutObjectReference: ..., objectType: ..., objectReference: ...}. Serialized as a JSON dict. If the signature is generated before anything is stored in the database (and has a PK), then the objectReference should be omitted from the payload but filled in afterwards.",
        max_length=1024,
        null=False,
        blank=False,
    )

    signature = models.CharField(
        verbose_name="signature",
        help_text="Signature of payload hash, the format of the signature should be specified by either verificationMethod or verificationJwsHeader",
        max_length=1024,
        null=False,
        blank=False,
    )

    verificationMethod = models.CharField(
        verbose_name="verificationMethod",
        help_text="A well-known string denoting which method is used. Valid values: <TBD>. We might expand this with a relation to which verification methods that are supported. There may be a minimal set of supported methods necessary.",
        max_length=1024,
        null=False,
        blank=False,
    )

    verificationPayload = models.CharField(
        verbose_name="verificationPayload",
        help_text="Internally generated serialized version of the data referenced by objectType and objectReference - by extracting and serializing their data as JSON.",
        max_length=1024,
        null=False,
        blank=False,
    )

    verificationPayloadHash = models.CharField(
        verbose_name="verificationPayloadHash",
        help_text="Internally generated cryptographic hash of the value to be signed, i.e. the value of verificationPayload",
        max_length=1024,
        null=False,
        blank=False,
    )

    verificationArtifact = models.CharField(
        verbose_name="verificationArtifact",
        help_text="A verification artifact in the form of a scanned object, image, signature etc.",
        max_length=1024,
        null=True,
        blank=True,
    )

    verificationSignedBy = models.CharField(
        verbose_name="verificationSignedBy",
        help_text="Because an identifier's information may change over time, there is a need to store that information at the time of signing. In case of a cryptographic signature, this field should contain some identifier for looking up or verifying the public key of the signing party. In case of a non-cryptographic signature, this field could contain a natural individual's names, personal number, email addresses - store a snapshot that binds to the signature at the time of signing. In case of a cryptographic signature, this may be the fingerprint of the individual's public key or in some cases, a token from the user's ID session.",
        max_length=1024,
        null=False,
        blank=False,
    )

    verificationSignedAs = models.CharField(
        verbose_name="verificationSignedAs",
        help_text="DRAFT FIELD: Specifies the relationship between the authorizing signature and the invidual which the payload concerns. This is relevant for Consent Records. Possible values: \"individual\" / \"delegate\"",
        max_length=1024,
        null=True,
        blank=True,
    )

    verificationJwsHeader = models.CharField(
        verbose_name="verificationJwsHeader",
        help_text="Alternative to the verificationMethod, verificationHash and verificationSignature, give a JWS serialized object (RFC7515)",
        max_length=1024,
        null=True,
        blank=True,
    )

    timestamp = models.CharField(
        verbose_name="timestamp",
        help_text="Timestamp of signature, currently this field isn't part of the payload so it's not tamper-proof.",
        max_length=1024,
        null=False,
        blank=False,
    )

    signedWithoutObjectReference = models.BooleanField(
        verbose_name="signedWithoutObjectReference",
        help_text="Indicates that objectReference was left blank in the serialized version that was signed.",
        null=True,
        blank=True,
    )

    objectType = models.CharField(
        verbose_name="objectType",
        help_text="Name of the schema model that objectReference points to. Values: \"signature\" or \"revision\"",
        max_length=1024,
        null=True,
        blank=True,
    )

    objectReference = models.CharField(
        verbose_name="objectReference",
        help_text="A symmetric relation / back reference to the objectType that was signed. We are currently just modelling signing another signature (a chain) or signing a Revision (which can be a revision of a consent record, an agreement, policy etc)",
        max_length=1024,
        null=True,
        blank=True,
    )



class AgreementLifecycle(models.Model):
    """TBD: Models the valid lifecycle states of an Agreement"""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Draft / Complete",
        max_length=1024,
        null=False,
        blank=False,
    )




