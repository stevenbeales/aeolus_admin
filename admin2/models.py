# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Concept(models.Model):
    concept_id = models.IntegerField(primary_key=True, verbose_name='Concept')
    concept_name = models.CharField(
        max_length=255, verbose_name='Concept Name')
    domain_id = models.CharField(max_length=20, verbose_name='Domain')
    vocabulary = models.ForeignKey(
        'Vocabulary', related_name='+', on_delete=models.CASCADE)
    concept_class_id = models.CharField(
        max_length=20, verbose_name='Concept Class')
    standard_concept = models.CharField(
        max_length=1, blank=True, null=True, verbose_name='Standard Concept')
    concept_code = models.CharField(max_length=50, verbose_name='Concept Code')
    valid_start_date = models.DateField(verbose_name='Valid Start Date')
    valid_end_date = models.DateField(verbose_name='Valid End Date')
    invalid_reason = models.CharField(
        max_length=1, blank=True, null=True, verbose_name='Invalid Reason')

    class Meta:
        managed = False
        db_table = 'concept'
        ordering = ['concept_name']

    def __str__(self):
        return f'{self.concept_name} ({self.concept_id})'


class ConceptAdmin(admin.ModelAdmin):
    date_hierarchy = 'valid_start_date'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class StandardCaseDrug(models.Model):
    primaryid = models.CharField(
        primary_key=True, max_length=512, blank=True)
    isr = models.CharField(max_length=512, blank=True, null=True)
    drug_seq = models.CharField(max_length=512, blank=True, null=True)
    role_cod = models.CharField(max_length=512, blank=True, null=True)
    standard_concept = models.ForeignKey(
        'Concept', related_name='+', on_delete=models.CASCADE,
        blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = 'standard_case_drug'
        verbose_name = "Standard Case Drug"
        unique_together = ('primaryid', 'isr')
        ordering = ['primaryid', 'isr', 'role_cod']

    def __str__(self):
        if self.primaryid == '':
            return f'{self.role_cod} ({self.isr})'
        else:
            return f'{self.role_cod} ({self.primaryid})'


class StandardCaseIndication(models.Model):
    primaryid = models.CharField(
        primary_key=True, max_length=512, blank=True)
    isr = models.CharField(max_length=512, blank=True, null=True)
    indi_drug_seq = models.CharField(max_length=512, blank=True, null=True)
    indi_pt = models.CharField(max_length=512, blank=True, null=True)
    indication_concept_id = models.IntegerField(blank=True, null=True)
    snomed_indication_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_case_indication'
        verbose_name = 'Standard Case Indication'
        unique_together = ('primaryid', 'isr')

    def __str__(self):
        return f'{self.primaryid} ({self.isr})'


class StandardCaseOutcome(models.Model):
    primaryid = models.CharField(
        primary_key=True, max_length=512, blank=True)
    isr = models.CharField(max_length=512, blank=True, null=True)
    pt = models.CharField(max_length=512, blank=True, null=True)
    outcome_concept_id = models.IntegerField(blank=True, null=True)
    snomed_outcome_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_case_outcome'
        verbose_name = 'Standard Case Outcome'
        unique_together = ('primaryid', 'isr')


class StandardCaseOutcomeCategory(models.Model):
    primaryid = models.CharField(
        primary_key=True, max_length=512, blank=True)
    isr = models.CharField(max_length=512, blank=True, null=True)
    outc_code = models.CharField(max_length=512, blank=True, null=True)
    snomed_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_case_outcome_category'
        verbose_name = 'Standard Case Outcome Category'
        verbose_name_plural = 'Standard Case Outcome Categories'
        unique_together = ('primaryid', 'isr')


class StandardDrugOutcomeContingencyTable(models.Model):
    drug_concept_id = models.IntegerField(
        blank=True, null=True)
    outcome_concept_id = models.IntegerField(
        primary_key=True, blank=True)
    count_a = models.IntegerField(blank=True, null=True)
    count_b = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    count_c = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    count_d = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_drug_outcome_contingency_table'
        verbose_name = 'Standard Drug Outcome Contingency Table'
        unique_together = ('drug_concept_id', 'outcome_concept_id')


class StandardDrugOutcomeCount(models.Model):
    drug_concept_id = models.IntegerField(blank=True, null=True)
    outcome_concept_id = models.IntegerField(primary_key=True, blank=True)
    drug_outcome_pair_count = models.IntegerField(blank=True, null=True)
    snomed_outcome_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_drug_outcome_count'
        verbose_name = 'Standard Drug Outcome Count'
        unique_together = ('drug_concept_id', 'outcome_concept_id')


class StandardDrugOutcomeDrilldown(models.Model):
    drug_concept_id = models.IntegerField(blank=True, null=True)
    outcome_concept_id = models.IntegerField(blank=True, null=True)
    snomed_outcome_concept_id = models.IntegerField(blank=True, null=True)
    primaryid = models.CharField(
        primary_key=True, max_length=512, blank=True)
    isr = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_drug_outcome_drilldown'
        verbose_name = 'Standard Drug Outcome Drilldown'
        unique_together = ('drug_concept_id', 'outcome_concept_id')


class StandardDrugOutcomeStatistics(models.Model):
    drug_concept_id = models.IntegerField(blank=True, null=True)
    outcome_concept_id = models.IntegerField(blank=True, null=True)
    snomed_outcome_concept_id = models.IntegerField(blank=True, null=True)
    case_count = models.IntegerField(blank=True, null=True)
    prr = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)
    prr_95_percent_upper_confidence_limit = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)
    prr_95_percent_lower_confidence_limit = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)
    ror = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)
    ror_95_percent_upper_confidence_limit = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)
    ror_95_percent_lower_confidence_limit = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_drug_outcome_statistics'
        verbose_name = 'Standard Drug Outcome Statistics'
        verbose_name_plural = 'Standard Drug Outcome Statistics'
        unique_together = ('drug_concept_id', 'outcome_concept_id')


class StandardUniqueAllCase(models.Model):
    caseid = models.CharField(max_length=512, blank=True, null=True)
    primaryid = models.CharField(
        primary_key=True, max_length=512, blank=True)
    isr = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_unique_all_case'
        verbose_name = 'Standard Unique All Case'
        unique_together = ('primaryid', 'isr')


class Vocabulary(models.Model):
    vocabulary_id = models.CharField(primary_key=True, max_length=20)
    vocabulary_name = models.CharField(max_length=255)
    vocabulary_reference = models.CharField(
        max_length=255, blank=True, null=True)
    vocabulary_version = models.CharField(
        max_length=255, blank=True, null=True)
    vocabulary_concept_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vocabulary'
        verbose_name_plural = 'Vocabularies'
        ordering = ['vocabulary_name']

    def __str__(self):
        return f'{self.vocabulary_name}'
