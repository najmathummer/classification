from django.views.generic import TemplateView
from django.views import View
import pandas
from sklearn.tree import DecisionTreeClassifier
from django.http import JsonResponse


url = 'dataset/breast-cancer-wisconsin.data.csv'
dataset = pandas.read_csv(url)
# Split-out validation dataset
array = dataset.values
X = array[:, 1:10]
print("\nVariables:- ")
print(X)
Y = array[:, 10]
print("\nClasses:- ")
print(Y)
model = DecisionTreeClassifier()
clf = model.fit(X, Y)


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class DiagnoseView(View):
    def post(self, request):
        input_array = []
        clump_thickness = request.POST.get('clump_thickness', '')
        uniformity_of_cell_size = request.POST.get('uniformityofCellSize', '')
        uniformity_of_Cell_Shape = request.POST.get(
            'uniformityofCellShape', '')
        marginal_Adhesion = request.POST.get('marginalAdhesion', '')
        single_Epithelial_Cell_Size = request.POST.get(
            'singleEpithelialCellSize', '')
        bare_Nuclei = request.POST.get('bareNuclei', '')
        bland_Chromatin = request.POST.get('blandChromatin', '')
        normal_Nucleoli = request.POST.get('normalNucleoli', '')
        mitosis = request.POST.get('mitoses', '')
        input_array.extend([clump_thickness, uniformity_of_cell_size, uniformity_of_Cell_Shape,
                           marginal_Adhesion, single_Epithelial_Cell_Size, bare_Nuclei, bland_Chromatin, normal_Nucleoli, mitosis])
        input_array = list(map(int, input_array))
        if(input_array[0] == 2):
            tumour = "benign"
        else:
            tumour  = "malignant"
        print(tumour)
        return JsonResponse(tumour, safe=False)