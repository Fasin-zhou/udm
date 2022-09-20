from cases.models import CasesModel
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist


class CasesModelListSerializers(serializers.ListSerializer):

    def create(self, validated_data):
        create_cases = [CasesModel(**item) for item in validated_data]
        return CasesModel.objects.bulk_create(create_cases)

    def update(self, instance, validated_data):
        cases_mapping = {case.id:case for case in instance}
        data_mapping = {item['id']:item for item in validated_data}

        case_in = []
        case_none = []
        for case_id,data in data_mapping.items():
            case = cases_mapping.get(case_id, None)
            if case is None:
                # 没有就创建，可改为没有就抛出错误
                # ret.append(self.child.create(data))
                # raise ObjectDoesNotExist(f'id={case_id} object does not exist')
                case_none.append(case_id)
            else:
                case_in.append({"case":case,"data":data})
                # ret.append(self.child.update(case, data))
        if case_none:
            raise ObjectDoesNotExist(f'id={case_none} object does not exist, please update again')
        else:
            for case_one in case_in:
                self.child.update(case_one['case'], case_one['data'])
        for case_id,case in cases_mapping.items():
            if case_id not in data_mapping:
                case.delete()

        return case_in


class CasesModelSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = CasesModel
        fields = '__all__'
        list_serializer_class = CasesModelListSerializers
    