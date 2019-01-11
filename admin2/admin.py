from django.contrib import admin

from .models import Concept, StandardCaseDrug, StandardCaseIndication, StandardCaseOutcome, \
    StandardDrugOutcomeDrilldown, StandardDrugOutcomeCount, StandardDrugOutcomeContingencyTable, \
    StandardCaseOutcomeCategory, StandardDrugOutcomeStatistics, StandardUniqueAllCase, Vocabulary


# Register your models here.

admin.site.register(Concept)
admin.site.register(StandardCaseDrug)
admin.site.register(StandardCaseIndication)
admin.site.register(StandardCaseOutcome)
admin.site.register(StandardCaseOutcomeCategory)
admin.site.register(StandardDrugOutcomeContingencyTable)
admin.site.register(StandardDrugOutcomeCount)
admin.site.register(StandardDrugOutcomeDrilldown)
admin.site.register(StandardDrugOutcomeStatistics)
admin.site.register(StandardUniqueAllCase)
admin.site.register(Vocabulary)
