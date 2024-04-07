import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GuidComponent } from './guid.component';

describe('GuidComponent', () => {
  let component: GuidComponent;
  let fixture: ComponentFixture<GuidComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GuidComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GuidComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
