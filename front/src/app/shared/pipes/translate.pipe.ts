import { Pipe, PipeTransform } from '@angular/core';
import { IDictOptions } from '../interfaces/components';

@Pipe({
  name: 'Translate',
  standalone: true,
})
export class TranslatePipe implements PipeTransform {
  transform(value: string | undefined, ...args: unknown[]): string {
    let translate_dict: IDictOptions = {
      THREATENING: 'AMEAÇA',
      GROPING: 'APALPAR',
      STALKING: 'PERSEGUIÇÂO',
      UNWANTED_COMMENTS: 'COMENTÁRIOS INDESEJADOS',
      FLASHING: 'PISCADA',
      UNWANTED_PHOTOS: 'FOTOS INDESEJADAS',
      OTHER: 'outro',
      CIS_MALE: 'Homem Cis',
      CIS_FEMALE: 'Mulher CIs',
      TRANS_FEMALE: 'Mulher Trans',
      TRANS_MALE: 'Homem Trans',
      BLACK: 'Negro',
      BROWN: 'Pardo',
      WHITE: 'Branco',
    };
    return value ? translate_dict[value] : 'Não informado';
  }
}