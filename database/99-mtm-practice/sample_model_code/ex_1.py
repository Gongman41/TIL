from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# 코드 예시
doctor1 = Doctor.objects.create(name='allie')
doctor2 = Doctor.objects.create(name='barbie')
patient1 = Patient.objects.create(name='carol', doctor=doctor1)
patient2 = Patient.objects.create(name='duke', doctor=doctor2)
patient3 = Patient.objects.create(name='carol', doctor=doctor2)
patient4 = Patient.objects.create(name='duke', doctor=doctor1, doctor2)
# 예약테이블을 따로 만들자. 환자쪽에 진료정보를 섞지 말자
#  -> 중개 모델
