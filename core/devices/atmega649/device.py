# Partname:  ATmega649
# generated automatically, do not edit
MCUREGS = {
	'ADMUX': '&124',
	  'ADMUX_REFS': '$C0',
	  'ADMUX_ADLAR': '$20',
	  'ADMUX_MUX': '$1F',
	'ADCSRA': '&122',
	  'ADCSRA_ADEN': '$80',
	  'ADCSRA_ADSC': '$40',
	  'ADCSRA_ADATE': '$20',
	  'ADCSRA_ADIF': '$10',
	  'ADCSRA_ADIE': '$08',
	  'ADCSRA_ADPS': '$07',
	'ADC': '&120',
	'ADCSRB': '&123',
	  'ADCSRB_ADTS': '$07',
	'DIDR0': '&126',
	  'DIDR0_ADC7D': '$80',
	  'DIDR0_ADC6D': '$40',
	  'DIDR0_ADC5D': '$20',
	  'DIDR0_ADC4D': '$10',
	  'DIDR0_ADC3D': '$08',
	  'DIDR0_ADC2D': '$04',
	  'DIDR0_ADC1D': '$02',
	  'DIDR0_ADC0D': '$01',
	'ACSR': '&80',
	  'ACSR_ACD': '$80',
	  'ACSR_ACBG': '$40',
	  'ACSR_ACO': '$20',
	  'ACSR_ACI': '$10',
	  'ACSR_ACIE': '$08',
	  'ACSR_ACIC': '$04',
	  'ACSR_ACIS': '$03',
	'DIDR1': '&127',
	  'DIDR1_AIN1D': '$02',
	  'DIDR1_AIN0D': '$01',
	'SPCR': '&76',
	  'SPCR_SPIE': '$80',
	  'SPCR_SPE': '$40',
	  'SPCR_DORD': '$20',
	  'SPCR_MSTR': '$10',
	  'SPCR_CPOL': '$08',
	  'SPCR_CPHA': '$04',
	  'SPCR_SPR': '$03',
	'SPSR': '&77',
	  'SPSR_SPIF': '$80',
	  'SPSR_WCOL': '$40',
	  'SPSR_SPI2X': '$01',
	'SPDR': '&78',
	'USIDR': '&186',
	'USISR': '&185',
	  'USISR_USISIF': '$80',
	  'USISR_USIOIF': '$40',
	  'USISR_USIPF': '$20',
	  'USISR_USIDC': '$10',
	  'USISR_USICNT': '$0F',
	'USICR': '&184',
	  'USICR_USISIE': '$80',
	  'USICR_USIOIE': '$40',
	  'USICR_USIWM': '$30',
	  'USICR_USICS': '$0C',
	  'USICR_USICLK': '$02',
	  'USICR_USITC': '$01',
	'UDR0': '&198',
	'UCSR0A': '&192',
	  'UCSR0A_RXC0': '$80',
	  'UCSR0A_TXC0': '$40',
	  'UCSR0A_UDRE0': '$20',
	  'UCSR0A_FE0': '$10',
	  'UCSR0A_DOR0': '$08',
	  'UCSR0A_UPE0': '$04',
	  'UCSR0A_U2X0': '$02',
	  'UCSR0A_MPCM0': '$01',
	'UCSR0B': '&193',
	  'UCSR0B_RXCIE0': '$80',
	  'UCSR0B_TXCIE0': '$40',
	  'UCSR0B_UDRIE0': '$20',
	  'UCSR0B_RXEN0': '$10',
	  'UCSR0B_TXEN0': '$08',
	  'UCSR0B_UCSZ02': '$04',
	  'UCSR0B_RXB80': '$02',
	  'UCSR0B_TXB80': '$01',
	'UCSR0C': '&194',
	  'UCSR0C_UMSEL0': '$40',
	  'UCSR0C_UPM0': '$30',
	  'UCSR0C_USBS0': '$08',
	  'UCSR0C_UCSZ0': '$06',
	  'UCSR0C_UCPOL0': '$01',
	'UBRR0': '&196',
	'SREG': '&95',
	  'SREG_I': '$80',
	  'SREG_T': '$40',
	  'SREG_H': '$20',
	  'SREG_S': '$10',
	  'SREG_V': '$08',
	  'SREG_N': '$04',
	  'SREG_Z': '$02',
	  'SREG_C': '$01',
	'SP': '&93',
	'MCUCR': '&85',
	  'MCUCR_PUD': '$10',
	  'MCUCR_IVSEL': '$02',
	  'MCUCR_IVCE': '$01',
	'MCUSR': '&84',
	  'MCUSR_JTRF': '$10',
	  'MCUSR_WDRF': '$08',
	  'MCUSR_BORF': '$04',
	  'MCUSR_EXTRF': '$02',
	  'MCUSR_PORF': '$01',
	'OSCCAL': '&102',
	'CLKPR': '&97',
	  'CLKPR_CLKPCE': '$80',
	  'CLKPR_CLKPS': '$0F',
	'PRR': '&100',
	  'PRR_PRLCD': '$10',
	  'PRR_PRTIM1': '$08',
	  'PRR_PRSPI': '$04',
	  'PRR_PRUSART0': '$02',
	  'PRR_PRADC': '$01',
	'SMCR': '&83',
	  'SMCR_SM': '$0E',
	  'SMCR_SE': '$01',
	'GPIOR2': '&75',
	'GPIOR1': '&74',
	'GPIOR0': '&62',
	'OCDR': '&81',
	'LCDDR18': '&254',
	'LCDDR17': '&253',
	'LCDDR16': '&252',
	'LCDDR15': '&251',
	'LCDDR13': '&249',
	'LCDDR12': '&248',
	'LCDDR11': '&247',
	'LCDDR10': '&246',
	'LCDDR8': '&244',
	'LCDDR7': '&243',
	'LCDDR6': '&242',
	'LCDDR5': '&241',
	'LCDDR3': '&239',
	'LCDDR2': '&238',
	'LCDDR1': '&237',
	'LCDDR0': '&236',
	'LCDCCR': '&231',
	'LCDFRR': '&230',
	  'LCDFRR_LCDPS': '$70',
	  'LCDFRR_LCDCD': '$07',
	'LCDCRB': '&229',
	  'LCDCRB_LCDCS': '$80',
	  'LCDCRB_LCD2B': '$40',
	  'LCDCRB_LCDMUX': '$30',
	  'LCDCRB_LCDPM': '$0F',
	'LCDCRA': '&228',
	  'LCDCRA_LCDEN': '$80',
	  'LCDCRA_LCDAB': '$40',
	  'LCDCRA_LCDIF': '$10',
	  'LCDCRA_LCDIE': '$08',
	  'LCDCRA_LCDBL': '$01',
	'EICRA': '&105',
	  'EICRA_ISC01': '$02',
	  'EICRA_ISC00': '$01',
	'EIMSK': '&61',
	  'EIMSK_PCIE': '$F0',
	  'EIMSK_INT0': '$01',
	'EIFR': '&60',
	  'EIFR_PCIF': '$F0',
	  'EIFR_INTF0': '$01',
	'PCMSK1': '&108',
	'PCMSK0': '&107',
	'EEAR': '&65',
	'EEDR': '&64',
	'EECR': '&63',
	  'EECR_EERIE': '$08',
	  'EECR_EEMWE': '$04',
	  'EECR_EEWE': '$02',
	  'EECR_EERE': '$01',
	'PORTA': '&34',
	'DDRA': '&33',
	'PINA': '&32',
	'PORTB': '&37',
	'DDRB': '&36',
	'PINB': '&35',
	'PORTC': '&40',
	'DDRC': '&39',
	'PINC': '&38',
	'PORTD': '&43',
	'DDRD': '&42',
	'PIND': '&41',
	'PORTE': '&46',
	'DDRE': '&45',
	'PINE': '&44',
	'PORTF': '&49',
	'DDRF': '&48',
	'PINF': '&47',
	'PORTG': '&52',
	'DDRG': '&51',
	'PING': '&50',
	'TCCR0A': '&68',
	  'TCCR0A_FOC0A': '$80',
	  'TCCR0A_WGM00': '$40',
	  'TCCR0A_COM0A': '$30',
	  'TCCR0A_WGM01': '$08',
	  'TCCR0A_CS0': '$07',
	'TCNT0': '&70',
	'OCR0A': '&71',
	'TIMSK0': '&110',
	  'TIMSK0_OCIE0A': '$02',
	  'TIMSK0_TOIE0': '$01',
	'TIFR0': '&53',
	  'TIFR0_OCF0A': '$02',
	  'TIFR0_TOV0': '$01',
	'GTCCR': '&67',
	  'GTCCR_TSM': '$80',
	  'GTCCR_PSR310': '$01',
	'TCCR1A': '&128',
	  'TCCR1A_COM1A': '$C0',
	  'TCCR1A_COM1B': '$30',
	  'TCCR1A_WGM1': '$03',
	'TCCR1B': '&129',
	  'TCCR1B_ICNC1': '$80',
	  'TCCR1B_ICES1': '$40',
	  'TCCR1B_WGM1': '$18',
	  'TCCR1B_CS1': '$07',
	'TCCR1C': '&130',
	  'TCCR1C_FOC1A': '$80',
	  'TCCR1C_FOC1B': '$40',
	'TCNT1': '&132',
	'OCR1A': '&136',
	'OCR1B': '&138',
	'ICR1': '&134',
	'TIMSK1': '&111',
	  'TIMSK1_ICIE1': '$20',
	  'TIMSK1_OCIE1B': '$04',
	  'TIMSK1_OCIE1A': '$02',
	  'TIMSK1_TOIE1': '$01',
	'TIFR1': '&54',
	  'TIFR1_ICF1': '$20',
	  'TIFR1_OCF1B': '$04',
	  'TIFR1_OCF1A': '$02',
	  'TIFR1_TOV1': '$01',
	'TCCR2A': '&176',
	  'TCCR2A_FOC2A': '$80',
	  'TCCR2A_WGM20': '$40',
	  'TCCR2A_COM2A': '$30',
	  'TCCR2A_WGM21': '$08',
	  'TCCR2A_CS2': '$07',
	'TCNT2': '&178',
	'OCR2A': '&179',
	'TIMSK2': '&112',
	  'TIMSK2_OCIE2A': '$02',
	  'TIMSK2_TOIE2': '$01',
	'TIFR2': '&55',
	  'TIFR2_OCF2A': '$02',
	  'TIFR2_TOV2': '$01',
	'ASSR': '&182',
	  'ASSR_EXCLK': '$10',
	  'ASSR_AS2': '$08',
	  'ASSR_TCN2UB': '$04',
	  'ASSR_OCR2UB': '$02',
	  'ASSR_TCR2UB': '$01',
	'WDTCR': '&96',
	  'WDTCR_WDCE': '$10',
	  'WDTCR_WDE': '$08',
	  'WDTCR_WDP': '$07',
	'SPMCSR': '&87',
	  'SPMCSR_SPMIE': '$80',
	  'SPMCSR_RWWSB': '$40',
	  'SPMCSR_RWWSRE': '$10',
	  'SPMCSR_BLBSET': '$08',
	  'SPMCSR_PGWRT': '$04',
	  'SPMCSR_PGERS': '$02',
	  'SPMCSR_SPMEN': '$01',
	'INT0Addr': '2',
	'PCINT0Addr': '4',
	'PCINT1Addr': '6',
	'TIMER2_COMPAddr': '8',
	'TIMER2_OVFAddr': '10',
	'TIMER1_CAPTAddr': '12',
	'TIMER1_COMPAAddr': '14',
	'TIMER1_COMPBAddr': '16',
	'TIMER1_OVFAddr': '18',
	'TIMER0_COMPAddr': '20',
	'TIMER0_OVFAddr': '22',
	'SPI__STCAddr': '24',
	'USART0__RXAddr': '26',
	'USART0__UDREAddr': '28',
	'USART0__TXAddr': '30',
	'USI_STARTAddr': '32',
	'USI_OVERFLOWAddr': '34',
	'ANALOG_COMPAddr': '36',
	'ADCAddr': '38',
	'EE_READYAddr': '40',
	'SPM_READYAddr': '42',
	'LCDAddr': '44'
}