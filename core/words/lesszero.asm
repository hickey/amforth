; ( n1 -- flag)
; Compare
; compare with zero
VE_LESSZERO:
    .dw $ff02
    .db "0<"
    .dw VE_HEAD
    .set VE_HEAD = VE_LESSZERO
XT_LESSZERO:
    .dw PFA_LESSZERO
PFA_LESSZERO:
    sbrc tosh,7
    rjmp PFA_TRUE1
    rjmp PFA_ZERO1
