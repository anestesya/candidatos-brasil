# -*- coding: utf-8 -*-
# Standard library imports
import csv
import codecs


# Third party imports


# Local apps imports


def UnicodeDictReader(utf8_data, **kwargs):
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        # yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])
        yield dict([(key, unicode(value, 'utf-8')) for key, value in row.iteritems()])


class LoadCSVs(object):

    def __init__(self):
        self.inidoneos = self._parse_file(codecs.open('csvs/inidoneos-csv.csv'))
        self.inabilitados = self._parse_file(codecs.open('csvs/inabilitados-csv.csv'))

    @staticmethod
    def _parse_file(f):
        d = {}
        for line in UnicodeDictReader(f):
            d[line['cpf_cnpj']] = line
        return d
