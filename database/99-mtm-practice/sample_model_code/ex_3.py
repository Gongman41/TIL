from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()
    # 작성된 곳의 물리적인 컬럼이 생기는 게 아니라 중개 모델을 만듦
    # 다대다관계에서 어디다가 넣어도 똑같음. 참조와 역참조 관계만 결정 


    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# Reservation Class 주석 처리


# 코드 예시
doctor1 = Doctor.objects.create(name='allie')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='duke')

patient1.doctors.add(doctor1)
patient1.doctors.all()
doctor1.patient_set.all()

doctor1.patient_set.add(patient2)
doctor1.patient_set.all()
patient2.doctors.all()
patient1.doctors.all()

doctor1.patient_set.remove(patient1)
doctor1.patient_set.all()
patient1.doctors.all()

patient2.patient_set.remove(doctor1)
patient2.doctors.all()
doctor1.patient_set.all()
